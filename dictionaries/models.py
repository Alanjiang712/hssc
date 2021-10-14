from django.db import models


class Service_role(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "服务角色"
		verbose_name_plural = "服务角色"


class Gender(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "性别"
		verbose_name_plural = "性别"


class Time_period_expression(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "时段表达"
		verbose_name_plural = "时段表达"


class Marital_status(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "婚姻状况"
		verbose_name_plural = "婚姻状况"


class Education(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "文化程度"
		verbose_name_plural = "文化程度"


class Institutions_list(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "机构清单"
		verbose_name_plural = "机构清单"


class Occupational_status(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "职业状况"
		verbose_name_plural = "职业状况"


class Nationality(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "民族"
		verbose_name_plural = "民族"


class Satisfaction(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "满意度"
		verbose_name_plural = "满意度"


class Medical_expenses_burden(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "医疗费用负担"
		verbose_name_plural = "医疗费用负担"


class Type_of_residence(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "居住类型"
		verbose_name_plural = "居住类型"


class Lips(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "口唇"
		verbose_name_plural = "口唇"


class Blood_type(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "血型"
		verbose_name_plural = "血型"


class Contract_signatory(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "合同签约户"
		verbose_name_plural = "合同签约户"


class Genetic_disease(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "遗传病"
		verbose_name_plural = "遗传病"


class Employee_list(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "职员表"
		verbose_name_plural = "职员表"


class Dentition(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "齿列"
		verbose_name_plural = "齿列"


class Drug_list(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "药品清单"
		verbose_name_plural = "药品清单"


class Pharynx(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "咽部"
		verbose_name_plural = "咽部"


class Family_relationship(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "家庭成员关系"
		verbose_name_plural = "家庭成员关系"


class Choose(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "选择"
		verbose_name_plural = "选择"


class Hearing(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "听力"
		verbose_name_plural = "听力"


class Life_event(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "生活事件"
		verbose_name_plural = "生活事件"


class Frequency(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "频次"
		verbose_name_plural = "频次"


class Athletic_ability(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "运动能力"
		verbose_name_plural = "运动能力"


class Degree_expression(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "程度表达"
		verbose_name_plural = "程度表达"


class Comparative_expression(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "比较表达"
		verbose_name_plural = "比较表达"


class Dorsal_artery_pulsation(models.Model):
	name = models.CharField(max_length=40, blank=True, null=True,  verbose_name="名称")
	score = models.SmallIntegerField(blank=True, null=True, verbose_name="分值")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "足背动脉搏动"
		verbose_name_plural = "足背动脉搏动"