from django.shortcuts import redirect
from django.contrib import admin

from hssc.site import clinic_site
# 导入自定义作业完成信号
from core.signals import operand_finished
from service.models import *


class HsscFormAdmin(admin.ModelAdmin):
    exclude = ["hssc_id", "label", "name", "customer", "operator", "creater", "pid", "cpid", "slug", "created_time", "updated_time", ]
    view_on_site = False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        base_form = 'base_form'
        extra_context['base_form'] = base_form
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def save_model(self, request, obj, form, change):
        # 发送服务作业完成信号
        pid = obj.pid.id
        ocode = 'RTC'
        uid = request.user.id
        form_data = request.POST.copy()
        form_data.pop('csrfmiddlewaretoken')
        form_data.pop('_save')
        operand_finished.send(sender=self, pid=pid, ocode=ocode, uid=uid, form_data=form_data)
        print('发送操作完成信号：', pid, ocode, uid, form_data)
        super().save_model(request, obj, form, change)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def response_change(self, request, obj):
        # 按照service.route_to的配置跳转
        redirect_option = obj.pid.service.route_to
        if redirect_option == 'CUSTOMER_HOMEPAGE':
            return redirect(obj.customer)
        else:
            return redirect('index')


class Men_zhen_chu_fang_biaoAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("药物处方", {"fields": ("boolfield_fu_yong_pin_ci", "boolfield_chang_yong_chu_fang_liang", "boolfield_yong_yao_zhou_qi", "boolfield_yong_yao_tu_jing", "relatedfield_drug_name", )}), )
    autocomplete_fields = ["boolfield_yong_yao_tu_jing", "relatedfield_drug_name", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Men_zhen_chu_fang_biao, Men_zhen_chu_fang_biaoAdmin)
clinic_site.register(Men_zhen_chu_fang_biao, Men_zhen_chu_fang_biaoAdmin)

class A6501Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("代人预约挂号", {"fields": ("datetimefield_ri_qi_shi_jian", "boolfield_ze_ren_ren", )}), )
    autocomplete_fields = ["boolfield_ze_ren_ren", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6501, A6501Admin)
clinic_site.register(A6501, A6501Admin)

class A6502Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("门诊分诊", {"fields": ("datetimefield_ri_qi_shi_jian", "boolfield_qian_dao_que_ren", "boolfield_ze_ren_ren", )}), )
    autocomplete_fields = ["boolfield_qian_dao_que_ren", "boolfield_ze_ren_ren", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6502, A6502Admin)
clinic_site.register(A6502, A6502Admin)

class A3101Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("体格检查表", {"fields": ("characterfield_right_eye_vision", "characterfield_left_eye_vision", "numberfield_body_temperature", "numberfield_pulse", "numberfield_respiratory_rate", "numberfield_hight", "numberfield_weight", "numberfield_body_mass_index", "numberfield_systolic_blood_pressure", "numberfield_diastolic_blood_pressure", "boolfield_yao_wei", "relatedfield_athletic_ability", "relatedfield_left_ear_hearing", "relatedfield_right_ear_hearing", "relatedfield_lips", "relatedfield_dentition", "relatedfield_pharynx", "relatedfield_lower_extremity_edema", )}), )
    autocomplete_fields = ["relatedfield_athletic_ability", "relatedfield_left_ear_hearing", "relatedfield_right_ear_hearing", "relatedfield_lips", "relatedfield_dentition", "relatedfield_pharynx", "relatedfield_lower_extremity_edema", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A3101, A3101Admin)
clinic_site.register(A3101, A3101Admin)

class Tang_niao_bing_zhuan_yong_wen_zhenAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("糖尿病专用问诊", {"fields": ("characterfield_supplementary_description_of_the_condition", "relatedfield_symptom_list", "boolfield_tang_niao_bing_zheng_zhuang", )}), )
    autocomplete_fields = ["relatedfield_symptom_list", "boolfield_tang_niao_bing_zheng_zhuang", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Tang_niao_bing_zhuan_yong_wen_zhen, Tang_niao_bing_zhuan_yong_wen_zhenAdmin)
clinic_site.register(Tang_niao_bing_zhuan_yong_wen_zhen, Tang_niao_bing_zhuan_yong_wen_zhenAdmin)

class Yao_shi_fu_wuAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("药事服务", {"fields": ("relatedfield_disease_name", "boolfield_shi_fou_ji_xu_shi_yong", "relatedfield_drug_name", )}), )
    autocomplete_fields = ["relatedfield_disease_name", "boolfield_shi_fou_ji_xu_shi_yong", "relatedfield_drug_name", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Yao_shi_fu_wu, Yao_shi_fu_wuAdmin)
clinic_site.register(Yao_shi_fu_wu, Yao_shi_fu_wuAdmin)

class Tang_niao_bing_zi_wo_jian_ceAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("糖尿病自我监测", {"fields": ("numberfield_kong_fu_xue_tang", )}), )
    
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Tang_niao_bing_zi_wo_jian_ce, Tang_niao_bing_zi_wo_jian_ceAdmin)
clinic_site.register(Tang_niao_bing_zi_wo_jian_ce, Tang_niao_bing_zi_wo_jian_ceAdmin)

class A6217Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("院内辅助问诊", {"fields": ("characterfield_supplementary_description_of_the_condition", "relatedfield_symptom_list", )}), )
    autocomplete_fields = ["relatedfield_symptom_list", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6217, A6217Admin)
clinic_site.register(A6217, A6217Admin)

class A6201Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("院外咨询", {"fields": ("characterfield_supplementary_description_of_the_condition", "relatedfield_symptom_list", "boolfield_chang_yong_zheng_zhuang", )}), )
    autocomplete_fields = ["relatedfield_symptom_list", "boolfield_chang_yong_zheng_zhuang", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6201, A6201Admin)
clinic_site.register(A6201, A6201Admin)

class A6218Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("门诊医生问诊", {"fields": ("characterfield_supplementary_description_of_the_condition", "relatedfield_symptom_list", )}), )
    autocomplete_fields = ["relatedfield_symptom_list", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6218, A6218Admin)
clinic_site.register(A6218, A6218Admin)

class T8901Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("非胰岛素依赖性糖尿病", {"fields": ("relatedfield_disease_name", "relatedfield_yi_lou_zhen_duan", "relatedfield_pai_chu_zhen_duan", )}), )
    autocomplete_fields = ["relatedfield_disease_name", "relatedfield_yi_lou_zhen_duan", "relatedfield_pai_chu_zhen_duan", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(T8901, T8901Admin)
clinic_site.register(T8901, T8901Admin)

class T6301Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("糖尿病一般随访", {"fields": ("boolfield_fu_yong_pin_ci", "boolfield_yao_pin_dan_wei", "relatedfield_drinking_frequency", "relatedfield_smoking_frequency", "boolfield_tang_niao_bing_zheng_zhuang", "relatedfield_drug_name", )}), 
        ("足背动脉检查", {"fields": ("relatedfield_left_foot", "relatedfield_right_foot", )}), 
        ("眼底检查", {"fields": ("relatedfield_fundus", )}), 
        ("血压监测", {"fields": ("numberfield_systolic_blood_pressure", "numberfield_diastolic_blood_pressure", )}), 
        ("空腹血糖检查", {"fields": ("numberfield_kong_fu_xue_tang", )}), )
    autocomplete_fields = ["boolfield_yao_pin_dan_wei", "relatedfield_drinking_frequency", "relatedfield_smoking_frequency", "boolfield_tang_niao_bing_zheng_zhuang", "relatedfield_drug_name", "relatedfield_left_foot", "relatedfield_right_foot", "relatedfield_fundus", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(T6301, T6301Admin)
clinic_site.register(T6301, T6301Admin)

class A6202Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("院外辅助问诊", {"fields": ("characterfield_supplementary_description_of_the_condition", "relatedfield_symptom_list", )}), )
    autocomplete_fields = ["relatedfield_symptom_list", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6202, A6202Admin)
clinic_site.register(A6202, A6202Admin)

class A6220Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("监测评估", {"fields": ("boolfield_yuan_wai_jian_kang_ping_gu", )}), )
    autocomplete_fields = ["boolfield_yuan_wai_jian_kang_ping_gu", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6220, A6220Admin)
clinic_site.register(A6220, A6220Admin)

class A6299Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("遗传病史", {"fields": ("boolfield_yi_chuan_ji_bing", "boolfield_yi_chuan_bing_shi_cheng_yuan", )}), 
        ("过敏史", {"fields": ("relatedfield_drug_name", )}), 
        ("家族病史", {"fields": ("boolfield_jia_zu_xing_ji_bing", "boolfield_jia_zu_bing_shi_cheng_yuan", )}), 
        ("手术史", {"fields": ("datetimefield_date", "relatedfield_name_of_operation", )}), 
        ("疾病史", {"fields": ("datetimefield_time_of_diagnosis", "boolfield_ge_ren_bing_shi", )}), 
        ("外伤史", {"fields": ("boolfield_wai_shang_ri_qi", "boolfield_wai_shang_xing_ji_bing", )}), 
        ("输血史", {"fields": ("numberfield_blood_transfusion", "boolfield_shu_xue_ri_qi", )}), 
        ("个人心理综合素质调查", {"fields": ("relatedfield_personality_tendency", "boolfield_shi_mian_qing_kuang", "boolfield_sheng_huo_gong_zuo_ya_li_qing_kuang", )}), 
        ("个人适应能力评估", {"fields": ("characterfield_working_hours_per_day", "relatedfield_are_you_satisfied_with_the_job_and_life", "relatedfield_are_you_satisfied_with_your_adaptability", )}), 
        ("个人身体健康评估", {"fields": ("relatedfield_own_health", "relatedfield_compared_to_last_year", "relatedfield_sports_preference", "relatedfield_exercise_time", "relatedfield_have_any_recent_symptoms_of_physical_discomfort", )}), 
        ("个人健康行为调查", {"fields": ("characterfield_average_sleep_duration", "characterfield_duration_of_insomnia", "relatedfield_drinking_frequency", "relatedfield_smoking_frequency", )}), 
        ("社会环境评估", {"fields": ("relatedfield_is_the_living_environment_satisfactory", "relatedfield_is_the_transportation_convenient", )}), )
    autocomplete_fields = ["boolfield_yi_chuan_ji_bing", "boolfield_yi_chuan_bing_shi_cheng_yuan", "relatedfield_drug_name", "boolfield_jia_zu_xing_ji_bing", "boolfield_jia_zu_bing_shi_cheng_yuan", "relatedfield_name_of_operation", "boolfield_ge_ren_bing_shi", "boolfield_wai_shang_xing_ji_bing", "relatedfield_personality_tendency", "boolfield_shi_mian_qing_kuang", "boolfield_sheng_huo_gong_zuo_ya_li_qing_kuang", "relatedfield_are_you_satisfied_with_the_job_and_life", "relatedfield_are_you_satisfied_with_your_adaptability", "relatedfield_own_health", "relatedfield_compared_to_last_year", "relatedfield_sports_preference", "relatedfield_exercise_time", "relatedfield_have_any_recent_symptoms_of_physical_discomfort", "relatedfield_drinking_frequency", "relatedfield_smoking_frequency", "relatedfield_is_the_living_environment_satisfactory", "relatedfield_is_the_transportation_convenient", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A6299, A6299Admin)
clinic_site.register(A6299, A6299Admin)

class A3502Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("尿常规检查", {"fields": ("boolfield_niao_tang", "boolfield_dan_bai_zhi", "boolfield_tong_ti", )}), )
    autocomplete_fields = ["boolfield_niao_tang", "boolfield_dan_bai_zhi", "boolfield_tong_ti", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(A3502, A3502Admin)
clinic_site.register(A3502, A3502Admin)

class Tang_niao_bing_cha_tiAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("眼底检查", {"fields": ("relatedfield_fundus", )}), 
        ("足背动脉检查", {"fields": ("relatedfield_left_foot", "relatedfield_right_foot", )}), )
    autocomplete_fields = ["relatedfield_fundus", "relatedfield_left_foot", "relatedfield_right_foot", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Tang_niao_bing_cha_ti, Tang_niao_bing_cha_tiAdmin)
clinic_site.register(Tang_niao_bing_cha_ti, Tang_niao_bing_cha_tiAdmin)

class Xue_ya_jian_ceAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("血压监测", {"fields": ("numberfield_systolic_blood_pressure", "numberfield_diastolic_blood_pressure", )}), )
    
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Xue_ya_jian_ce, Xue_ya_jian_ceAdmin)
clinic_site.register(Xue_ya_jian_ce, Xue_ya_jian_ceAdmin)

class Kong_fu_xue_tang_jian_chaAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("空腹血糖检查", {"fields": ("numberfield_kong_fu_xue_tang", )}), )
    
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Kong_fu_xue_tang_jian_cha, Kong_fu_xue_tang_jian_chaAdmin)
clinic_site.register(Kong_fu_xue_tang_jian_cha, Kong_fu_xue_tang_jian_chaAdmin)

class Tang_hua_xue_hong_dan_bai_jian_cha_biaoAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("糖化血红蛋白检查", {"fields": ("numberfield_tang_hua_xue_hong_dan_bai", )}), )
    
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Tang_hua_xue_hong_dan_bai_jian_cha_biao, Tang_hua_xue_hong_dan_bai_jian_cha_biaoAdmin)
clinic_site.register(Tang_hua_xue_hong_dan_bai_jian_cha_biao, Tang_hua_xue_hong_dan_bai_jian_cha_biaoAdmin)

class T9001Admin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("非胰岛素依赖性糖尿病", {"fields": ("relatedfield_disease_name", "relatedfield_yi_lou_zhen_duan", "relatedfield_pai_chu_zhen_duan", )}), )
    autocomplete_fields = ["relatedfield_disease_name", "relatedfield_yi_lou_zhen_duan", "relatedfield_pai_chu_zhen_duan", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(T9001, T9001Admin)
clinic_site.register(T9001, T9001Admin)

class Qian_yue_fu_wuAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("家庭医生签约", {"fields": ("boolfield_jia_ting_qian_yue_fu_wu_xie_yi", "boolfield_qian_yue_que_ren", "boolfield_ze_ren_ren", )}), )
    autocomplete_fields = ["boolfield_qian_yue_que_ren", "boolfield_ze_ren_ren", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Qian_yue_fu_wu, Qian_yue_fu_wuAdmin)
clinic_site.register(Qian_yue_fu_wu, Qian_yue_fu_wuAdmin)

class Shu_ye_zhu_sheAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("输液注射单", {"fields": ("boolfield_fu_yong_pin_ci", "boolfield_yao_pin_gui_ge", "boolfield_chang_yong_chu_fang_liang", "boolfield_zhi_xing_qian_ming", "boolfield_yong_yao_zhou_qi", "boolfield_zhu_she_ri_qi", "relatedfield_drug_name", )}), )
    autocomplete_fields = ["relatedfield_drug_name", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Shu_ye_zhu_she, Shu_ye_zhu_sheAdmin)
clinic_site.register(Shu_ye_zhu_she, Shu_ye_zhu_sheAdmin)

class Ju_min_ji_ben_xin_xi_diao_chaAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("个人基本信息", {"fields": ("characterhssc_identification_number", "characterfield_resident_file_number", "characterfield_family_address", "characterfield_medical_ic_card_number", "characterfield_contact_number", "characterfield_name", "datetimefield_date_of_birth", "relatedfield_gender", "relatedfield_nationality", "relatedfield_marital_status", "relatedfield_education", "relatedfield_occupational_status", "relatedfield_medical_expenses_burden", "relatedfield_type_of_residence", "relatedfield_blood_type", "relatedfield_signed_family_doctor", "relatedfield_family_relationship", )}), )
    autocomplete_fields = ["relatedfield_gender", "relatedfield_nationality", "relatedfield_marital_status", "relatedfield_education", "relatedfield_occupational_status", "relatedfield_medical_expenses_burden", "relatedfield_type_of_residence", "relatedfield_blood_type", "relatedfield_signed_family_doctor", "relatedfield_family_relationship", ]
    readonly_fields = []
admin.site.register(Ju_min_ji_ben_xin_xi_diao_cha, Ju_min_ji_ben_xin_xi_diao_chaAdmin)
clinic_site.register(Ju_min_ji_ben_xin_xi_diao_cha, Ju_min_ji_ben_xin_xi_diao_chaAdmin)

class Shen_qing_kong_fu_xue_tang_jian_cha_fu_wuAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": (("characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ),)}), 
        ("申请服务表", {"fields": ("boolfield_dang_qian_pai_dui_ren_shu", "boolfield_yu_ji_deng_hou_shi_jian", "boolfield_ze_ren_ren", "boolfield_fu_wu_xiang_mu_ming_cheng", "boolfield_an_pai_que_ren", )}), )
    autocomplete_fields = ["boolfield_ze_ren_ren", "boolfield_fu_wu_xiang_mu_ming_cheng", "boolfield_an_pai_que_ren", ]
    readonly_fields = ["characterfield_contact_address", "characterfield_contact_number", "characterfield_name", "characterfield_gender", "characterfield_age", ]
admin.site.register(Shen_qing_kong_fu_xue_tang_jian_cha_fu_wu, Shen_qing_kong_fu_xue_tang_jian_cha_fu_wuAdmin)
clinic_site.register(Shen_qing_kong_fu_xue_tang_jian_cha_fu_wu, Shen_qing_kong_fu_xue_tang_jian_cha_fu_wuAdmin)

class Yao_pin_ji_ben_xin_xi_diao_chaAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("药品基本信息表", {"fields": ("boolfield_yao_pin_ming_cheng", "boolfield_fu_yong_pin_ci", "boolfield_yao_pin_bian_ma", "boolfield_yao_pin_gui_ge", "boolfield_chang_yong_chu_fang_liang", "boolfield_dui_zhao_yi_bao_ming_cheng", "boolfield_dui_zhao_ji_yao_ming_cheng", "boolfield_huan_suan_gui_ze", "boolfield_yong_yao_zhou_qi", "boolfield_chu_fang_ji_liang_dan_wei", "boolfield_ru_ku_ji_liang_dan_wei", "boolfield_xiao_shou_ji_liang_dan_wei", "boolfield_yong_yao_tu_jing", "boolfield_yao_pin_fen_lei", )}), )
    autocomplete_fields = ["boolfield_chu_fang_ji_liang_dan_wei", "boolfield_ru_ku_ji_liang_dan_wei", "boolfield_xiao_shou_ji_liang_dan_wei", "boolfield_yong_yao_tu_jing", "boolfield_yao_pin_fen_lei", ]
    readonly_fields = []
admin.site.register(Yao_pin_ji_ben_xin_xi_diao_cha, Yao_pin_ji_ben_xin_xi_diao_chaAdmin)
clinic_site.register(Yao_pin_ji_ben_xin_xi_diao_cha, Yao_pin_ji_ben_xin_xi_diao_chaAdmin)

class Gong_ying_shang_ji_ben_xin_xi_diao_chaAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("物料供应商基本信息表", {"fields": ("characterfield_contact_address", "boolfield_gong_ying_shang_bian_ma", "boolfield_zhu_yao_gong_ying_chan_pin", "boolfield_gong_huo_zhou_qi", "boolfield_gong_ying_shang_ming_cheng", "characterfield_contact_number", "boolfield_xin_yu_ping_ji", )}), )
    autocomplete_fields = ["boolfield_xin_yu_ping_ji", ]
    readonly_fields = []
admin.site.register(Gong_ying_shang_ji_ben_xin_xi_diao_cha, Gong_ying_shang_ji_ben_xin_xi_diao_chaAdmin)
clinic_site.register(Gong_ying_shang_ji_ben_xin_xi_diao_cha, Gong_ying_shang_ji_ben_xin_xi_diao_chaAdmin)

class She_bei_ji_ben_xin_xi_ji_luAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("设备基本信息表", {"fields": ("boolfield_she_bei_bian_ma", "boolfield_sheng_chan_chang_jia", "boolfield_she_bei_fu_wu_dan_wei_hao_shi", "boolfield_she_bei_jian_xiu_zhou_qi", "boolfield_she_bei_shi_yong_cheng_ben", "boolfield_she_bei_ming_cheng", "characterfield_contact_number", "boolfield_she_bei_shi_yong_fu_wu_gong_neng", )}), )
    autocomplete_fields = ["boolfield_she_bei_shi_yong_fu_wu_gong_neng", ]
    readonly_fields = []
admin.site.register(She_bei_ji_ben_xin_xi_ji_lu, She_bei_ji_ben_xin_xi_ji_luAdmin)
clinic_site.register(She_bei_ji_ben_xin_xi_ji_lu, She_bei_ji_ben_xin_xi_ji_luAdmin)

class Fu_wu_fen_gong_ji_gou_ji_ben_xin_xi_diao_chaAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("服务分供机构基本信息表", {"fields": ("characterfield_contact_address", "boolfield_ji_gou_dai_ma", "boolfield_ji_gou_shu_xing", "boolfield_gong_ying_shang_bian_ma", "boolfield_zhuan_ye_fu_wu", "boolfield_gong_ying_shang_ming_cheng", "characterfield_contact_number", "boolfield_xin_yu_ping_ji", )}), )
    autocomplete_fields = ["boolfield_xin_yu_ping_ji", ]
    readonly_fields = []
admin.site.register(Fu_wu_fen_gong_ji_gou_ji_ben_xin_xi_diao_cha, Fu_wu_fen_gong_ji_gou_ji_ben_xin_xi_diao_chaAdmin)
clinic_site.register(Fu_wu_fen_gong_ji_gou_ji_ben_xin_xi_diao_cha, Fu_wu_fen_gong_ji_gou_ji_ben_xin_xi_diao_chaAdmin)

class Zhi_yuan_ji_ben_xin_xi_wei_huAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("职员基本信息表", {"fields": ("characterhssc_identification_number", "characterfield_practice_qualification", "characterfield_expertise", "characterfield_practice_time", "boolfield_zhi_yuan_bian_ma", "characterfield_contact_number", "characterfield_name", "relatedfield_affiliation", "relatedfield_service_role", )}), )
    autocomplete_fields = ["relatedfield_affiliation", "relatedfield_service_role", ]
    readonly_fields = []
admin.site.register(Zhi_yuan_ji_ben_xin_xi_wei_hu, Zhi_yuan_ji_ben_xin_xi_wei_huAdmin)
clinic_site.register(Zhi_yuan_ji_ben_xin_xi_wei_hu, Zhi_yuan_ji_ben_xin_xi_wei_huAdmin)

class Ji_gou_ji_ben_xin_xi_wei_huAdmin(HsscFormAdmin):
    fieldsets = (("基本信息", {"fields": ((),)}), 
        ("机构基本信息表", {"fields": ("characterfield_contact_address", "boolfield_ji_gou_bian_ma", "boolfield_ji_gou_ming_cheng", "boolfield_ji_gou_dai_ma", "boolfield_ji_gou_shu_xing", "boolfield_ji_gou_ceng_ji", "boolfield_suo_zai_hang_zheng_qu_hua_dai_ma", "boolfield_xing_zheng_qu_hua_gui_shu", "boolfield_fa_ding_fu_ze_ren", "characterfield_contact_number", )}), )
    
    readonly_fields = []
admin.site.register(Ji_gou_ji_ben_xin_xi_wei_hu, Ji_gou_ji_ben_xin_xi_wei_huAdmin)
clinic_site.register(Ji_gou_ji_ben_xin_xi_wei_hu, Ji_gou_ji_ben_xin_xi_wei_huAdmin)
