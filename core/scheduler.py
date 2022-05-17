from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from enum import Enum
import datetime
from registration.signals import user_registered, user_activated, user_approved

from core.hsscbase_class import FieldsType
from core.models import Service, ServiceRule, Staff, Customer, OperationProc, StaffTodo, RecommendedService, Message
from core.utils import field_name_replace
from core.signals import operand_started, operand_finished  # 自定义作业完成信号
from service.models import *


@receiver(user_logged_in)
def user_logged_in_handler(sender, user, request, **kwargs):
    '''
    系统内置业务事件的信号处理：用户注册，用户登录，员工登录
    收到登录信号，生成用户/职员登录事件
    '''
    # 用户登录Session登记
    from analytics.models import record_login
    record_login(request, user)

    # 获得登陆作业进程参数
    if user.is_staff:  # 职员登录
        event_name = 'doctor_login'
        customer = None
        operator = creater = user.customer
        print('职员登录', user, event_name)
    else:
        event_name = 'user_login'   # 客户登录
        customer = operator = creater = user.customer
        print('客户登录', user, event_name)

    # 创建一个状态为“已完成”的职员/客户登录作业进程
    new_proc=OperationProc.objects.create(
        service=Service.objects.get(name=event_name),  # 服务
        customer=customer,  # 客户
        operator=operator,  # 作业人员
        creater=creater,  # 创建者
        state=4,  # 进程状态：登录完成
    )

    # 发送登录作业完成信号
    operand_finished.send(sender=user_logged_in_handler, pid=new_proc)


# 收到注册成功信号，生成用户注册事件：registration.signals.user_registered
@receiver(user_registered)
def user_registered_handler(sender, user, request, **kwargs):
    # 获得注册作业进程参数
    if user.is_staff:  # 职员注册
        event_name = 'staff_registered'
        customer = None
        operator = creater = user.customer
        print('职员注册', user, event_name)
    else:
        event_name = 'Z6201'   # 客户注册
        customer = operator = creater = user.customer
        print('客户注册', user, event_name)

    # 创建一个状态为“已完成”的职员/客户注册作业进程
    new_proc=OperationProc.objects.create(
        service=Service.objects.get(name=event_name),  # 服务
        customer=customer,  # 客户
        operator=operator,  # 作业人员
        creater=creater,  # 创建者
        state=4,  # 进程状态：注册完成
    )

    # 发送注册作业完成信号
    operand_finished.send(sender=user_registered_handler, pid=new_proc)


@receiver(post_save, sender=User)
def user_post_save_handler(sender, instance, created, **kwargs):
    if created:  # 创建用户
        if instance.is_staff:  # 新建职员
            print('创建员工信息', instance)
            customer = Customer.objects.create(
                user=instance,
                name=instance.last_name+instance.first_name,
            )
            Staff.objects.create(
                customer=customer,
                email=instance.email,
            )
        else:  # 新建客户
            print('创建客户信息', instance)
            name = instance.last_name+instance.first_name if instance.last_name+instance.first_name else instance.username
            Customer.objects.create(
                user=instance,
                name=name,
            )
    # else:   # 更新用户
    #     if instance.is_staff:
    #         print('更新员工信息', instance)
    #         customer = instance.customer
    #         customer.name = instance.last_name+instance.first_name
    #         customer.save()
    #         customer.staff.email = instance.email
    #         customer.staff.save()
    #     else:   # 客户
    #         print('更新客户信息', instance)
    #         customer = instance.customer
    #         customer.name = instance.last_name+instance.first_name
    #         customer.save()


@receiver(post_delete, sender=User)
def user_post_delete_handler(sender, instance, **kwargs):
    '''
    删除用户后同步删除Customer和Staff相关信息
    '''
    if instance.is_staff:
        print('删除员工信息', instance)
        try:
            customer = instance.customer
            customer.staff.delete()
            instance.customer.delete()
        except:
            pass
    else:
        try:
            print('删除客户信息', instance)
            instance.customer.delete()
        except:
            pass


@receiver(post_save, sender=OperationProc)
def operation_proc_post_save_handler(sender, instance, created, **kwargs):

    # if not created and instance.state == 4 and not instance.service.is_system_service :  # 表单作业完成(state=4)
    #     # 发送服务作业完成信号
    #     operand_finished.send(sender=operation_proc_post_save_handler, pid=instance)


    # 根据服务进程创建待办事项: sync_proc_todo_list
    if instance.operator and instance.customer:
        try :
            todo = instance.stafftodo
            todo.scheduled_time = instance.scheduled_time
            todo.state = instance.state
            todo.priority = instance.priority
            todo.save()
        except StaffTodo.DoesNotExist:
            todo = StaffTodo.objects.create(
                operation_proc=instance,
                operator=instance.operator,
                scheduled_time=instance.scheduled_time,
                state=instance.state,
                customer_number=instance.customer.name,
                customer_name=instance.customer.name,
                service_label=instance.service.label,
                customer_phone=instance.customer.phone,
                customer_address=instance.customer.address,
                priority = instance.priority
            )


@receiver(operand_started)
def operand_started_handler(sender, **kwargs):
    operation_proc = kwargs['operation_proc']  # 作业进程
    operation_proc.update_state(kwargs['ocode'])  # 更新作业进程操作码    
    operation_proc.operator = kwargs['operator']  # 设置当前用户为作业进程操作员
    operation_proc.save()


@receiver(operand_finished)
def operand_finished_handler(sender, **kwargs):
    def _get_scanned_data(event_rule, operation_proc, expression_fields_set):
        # 1. 根据detection_scope生成待检测数据集合
        if event_rule.detection_scope == 'CURRENT_SERVICE':
            _scanned_data = operation_proc.customer.get_health_record_by_pid(operation_proc)
        else:
            period = None  # 意味着self.detection_scope == 'ALL'表示获取全部健康记录
            if event_rule.detection_scope == 'LAST_WEEK_SERVICES':  # 获取表示指定时间段内的健康记录
                start_time = datetime.datetime.now() + datetime.timedelta(days=-7)
                end_time = datetime.datetime.now()
                period = (start_time, end_time)
            _scanned_data = operation_proc.customer.get_health_record_by_period(period)  # 返回客户健康档案记录dict
        print('From scheduler._get_scanned_data: 1. _scanned_data:', event_rule.detection_scope, _scanned_data)

        # 2. 根据表达式字段集合剪裁生成待检测数据字典
        scanned_data = {}
        for field_name in expression_fields_set:
            scanned_data[field_name] = _scanned_data.get(field_name, '')
        print('From scheduler._get_scanned_data: 2. scanned_data:', scanned_data)

        # 3. 生成符合field_name_replace()要求格式的待检测数据集合
        for field_name, field_val in scanned_data.items():
            # 先获取字段类型
            field_type = eval(f'FieldsType.{field_name}').value
            if field_type == 'Datetime' or field_type == 'Date':  # 日期类型暂时不处理
                scanned_data[field_name] = f'{field_val}'
            elif field_type == 'Numbers':  # 如果字段类型是Numbers，直接使用字符串数值
                scanned_data[field_name] = f'{field_val}'
            else:  # 如果字段类型是String或关联字段，转换为集合字符串
                print('From scheduler._get_scanned_data: String或关联字段', field_type, scanned_data[field_name])
                if field_val:
                    scanned_data[field_name] = f'{set(field_val)}'
                else:
                    scanned_data[field_name] = '{}'
        print('From scheduler._get_scanned_data: 3.结果scanned_data：', scanned_data)
        return scanned_data

    def _is_rule_satified(event_rule, operation_proc):
        '''
        检查表达式是否满足 return: Boolean
        parameters: form_data, self.expression
		'''
        if event_rule.expression == 'completed':  # 完成事件直接返回
            return True
        else:  # 判断是否发生其他业务事件
            # 数据预处理
            expression_fields_set = set(event_rule.expression_fields.strip().split(','))  # self.expression_fields: 去除空格，转为数组，再转为集合去重
            scanned_data_dict = _get_scanned_data(event_rule, operation_proc, expression_fields_set)  # 获取待扫描字段数据的字符格式字典，适配field_name_replace()的格式要求
            print('From EventRule.is_satified 检查表达式:', event_rule.expression)
            print('检查字段:', expression_fields_set)            
            print('扫描内容:', scanned_data_dict)

            expression_fields_val_dict = {}  # 构造一个仅存储表达式内的字段及值的字典
            for field_name in expression_fields_set:
                expression_fields_val_dict[field_name] = scanned_data_dict.get(field_name, '')            

            print('表达式字段及值:', expression_fields_val_dict)
            result = eval(field_name_replace(event_rule.expression, expression_fields_val_dict))  # 待检查的字段值带入表达式，并执行返回结果
            return result

    def _get_set_value(field_type, id_list):
        if not id_list:
            return ''
        else:
            # 转换id列表为对应的字典值列表
            _model_list = field_type.split('.')  # 分割模型名称field_type: app_label.model_name
            app_label = _model_list[0]  # 应用名称
            model_name = _model_list[1]  # 模型名称
            class ConvertIdToValue(Enum):
                icpc = map(lambda x: eval(model_name).objects.get(id=x).iname, id_list)
                dictionaries = map(lambda x: eval(model_name).objects.get(id=x).value, id_list)
                # medcine = map(lambda x: eval(model_name).objects.get(id=x).name, id_list)
            val_iterator = eval(f'ConvertIdToValue.{app_label}').value
            return str(set(val_iterator))

    def _create_next_service(**kwargs):
        '''
        生成后续服务
        '''
        # 准备新的服务作业进程参数
        operation_proc = kwargs['operation_proc']
        customer = operation_proc.customer
        operator = kwargs['operator']
        service = kwargs['next_service']
        contract_service_proc = operation_proc.contract_service_proc
        content_type = ContentType.objects.get(app_label='service', model=kwargs['next_service'].name.lower())
        # 创建新的服务作业进程
        new_proc=OperationProc.objects.create(
            service=service,  # 服务
            customer=customer,  # 客户
            creater=operator,  # 创建者
            state=0,  # 进程状态
            scheduled_time=datetime.datetime.now(),  # 创建时间
            parent_proc=operation_proc,  # 当前进程是被创建进程的父进程
            contract_service_proc=contract_service_proc,  # 所属合约服务进程
            content_type=content_type,  # 表单类型
        )
        # Here postsave signal in service.models
        # 更新允许作业岗位
        role = service.role.all()
        new_proc.role.set(role)

        form = create_form_instance(new_proc)
        # 更新OperationProc服务进程的form实例信息
        new_proc.object_id = form.id
        new_proc.entry = f'/clinic/service/{new_proc.service.name.lower()}/{form.id}/change'
        new_proc.save()


        return f'创建服务作业进程: {new_proc}'

    def _recommend_next_service(**kwargs):
        '''
        推荐后续服务
        '''
        # 准备新的服务作业进程参数
        operation_proc = kwargs['operation_proc']
        # 创建新的服务作业进程
        _recommended = RecommendedService.objects.create(
            service=kwargs['next_service'],  # 推荐的服务
            customer=operation_proc.customer,  # 客户
            creater=kwargs['operator'],  # 创建者
            pid=operation_proc,  # 当前进程是被推荐服务的父进程
            cpid=operation_proc.contract_service_proc,  # 所属合约服务进程
        )
        return f'推荐服务作业: {_recommended}'

    def _alert_content_violations(self, **kwargs):
        '''
        内容违规提示
        '''
        print('alert_content_violations:', '内容违规提示')
        return '内容违规提示'

    def _send_notification(**kwargs):
        '''
        发送提醒
        '''
        # 准备服务作业进程参数
        operation_proc = kwargs['operation_proc']

        # 获取提醒人员list
        _reminders_option = kwargs['reminders']
        reminders = _get_reminders(_reminders_option)

        # 创建提醒消息
        for customer in reminders:
            _ = Message.objects.create(
                message=kwargs['message'],  # 消息内容
                customer=customer,  # 客户
                creater=kwargs['operator'],  # 创建者
                pid=operation_proc,  # 当前进程是被推荐服务的父进程
                cpid=operation_proc.contract_service_proc,  # 所属合约服务进程
            )

        def _get_reminders(_option):
            '''
            用选项值为list.index获取提醒对象列表
            '''
            reminder_option = [
                operation_proc.customer,  # 0: 发送给当前客户
                kwargs['operator'],  # 1: 发送给当前作业人员
                # return workgroup_list,  # 2: 发送给当前作业组成员
            ]
            return [reminder_option[_option]]

        return f'生成提醒消息OK'

    def _execute_system_operand(system_operand, **kwargs):
        '''
        执行系统自动作业
        '''
        class SystemOperandFunc(Enum):
            CREATE_NEXT_SERVICE = _create_next_service  # 生成后续服务
            RECOMMEND_NEXT_SERVICE = _recommend_next_service  # 推荐后续服务
            VIOLATION_ALERT = _alert_content_violations  # 内容违规提示
            SEND_NOTIFICATION = _send_notification  # 发送提醒

		# 调用OperandFuncMixin中的系统自动作业函数
        return eval(f'SystemOperandFunc.{system_operand}')(**kwargs)

    operation_proc = kwargs['pid']

    # 更新作业进程状态为RTC
    operation_proc.update_state('RTC')

    # 根据服务规则检查业务事件是否发生，执行系统作业
    # 逐一检查service_rule.event_rule.expression是否满足
    for service_rule in ServiceRule.objects.filter(service=operation_proc.service, is_active=True):
        # 如果event_rule.expression为真，则构造事件参数，生成业务事件
        if _is_rule_satified(service_rule.event_rule, operation_proc):
            print('From check_rules 满足规则：', service_rule.service, service_rule.event_rule)
            # 构造作业参数
            operation_params = {
                'operation_proc': operation_proc,
                'operator': operation_proc.operator,
                'service': service_rule.service,
                'next_service': service_rule.next_service,
                'passing_data': service_rule.passing_data,
                'complete_feedback': service_rule.complete_feedback,
                'reminders': service_rule.reminders,
                'message': service_rule.message,
                'interval_rule': service_rule.interval_rule,
                'interval_time': service_rule.interval_time,
            }
            # 执行系统自动作业。传入：作业指令，作业参数；返回：String，描述执行结果
            _result = _execute_system_operand(service_rule.system_operand, **operation_params)
            print('From check_rules 执行结果:', _result)
