# Generated by Django 3.2.6 on 2022-05-19 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ji_gou_ji_ben_xin_xi_biao',
            options={'verbose_name': '机构基本信息维护', 'verbose_name_plural': '机构基本信息维护'},
        ),
        migrations.AlterModelOptions(
            name='she_bei_ji_ben_xin_xi_ji_lu',
            options={'verbose_name': '设备基本信息维护', 'verbose_name_plural': '设备基本信息维护'},
        ),
        migrations.AlterModelOptions(
            name='zhi_yuan_ji_ben_xin_xi_biao',
            options={'verbose_name': '职员基本信息维护', 'verbose_name_plural': '职员基本信息维护'},
        ),
        migrations.RemoveField(
            model_name='a3101',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a3101',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a3101',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a3502',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a3502',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a3502',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6201',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6201',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6201',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6202',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6202',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6202',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6217',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6217',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6217',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6218',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6218',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6218',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6220',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6220',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6220',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6299',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6299',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6299',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6501',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6501',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6501',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='a6502',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='a6502',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='a6502',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='kong_fu_xue_tang_jian_cha',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='kong_fu_xue_tang_jian_cha',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='kong_fu_xue_tang_jian_cha',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='men_zhen_chu_fang_biao',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='men_zhen_chu_fang_biao',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='men_zhen_chu_fang_biao',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='qian_yue_fu_wu',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='qian_yue_fu_wu',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='qian_yue_fu_wu',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='shen_qing_kong_fu_xue_tang_jian_cha_fu_wu',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='shen_qing_kong_fu_xue_tang_jian_cha_fu_wu',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='shen_qing_kong_fu_xue_tang_jian_cha_fu_wu',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='shu_ye_zhu_she',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='shu_ye_zhu_she',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='shu_ye_zhu_she',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='t6301',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='t6301',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='t6301',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='t8901',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='t8901',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='t8901',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='t9001',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='t9001',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='t9001',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='tang_hua_xue_hong_dan_bai_jian_cha_biao',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='tang_hua_xue_hong_dan_bai_jian_cha_biao',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='tang_hua_xue_hong_dan_bai_jian_cha_biao',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_cha_ti',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_cha_ti',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_cha_ti',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_zhuan_yong_wen_zhen',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_zhuan_yong_wen_zhen',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_zhuan_yong_wen_zhen',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_zi_wo_jian_ce',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_zi_wo_jian_ce',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='tang_niao_bing_zi_wo_jian_ce',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='xue_ya_jian_ce',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='xue_ya_jian_ce',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='xue_ya_jian_ce',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='yao_shi_fu_wu',
            name='characterfield_age',
        ),
        migrations.RemoveField(
            model_name='yao_shi_fu_wu',
            name='characterfield_contact_address',
        ),
        migrations.RemoveField(
            model_name='yao_shi_fu_wu',
            name='characterfield_gender',
        ),
        migrations.AddField(
            model_name='a3101',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a3101',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a3101',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A3101', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a3502',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a3502',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a3502',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A3502', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6201',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6201',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6201',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6201', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6202',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6202',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6202',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6202', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6217',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6217',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6217',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6217', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6218',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6218',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6218',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6218', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6220',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6220',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6220',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6220', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6299',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6299',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6299',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6299', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6501',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6501',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6501',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6501', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='a6502',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='a6502',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='a6502',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_A6502', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='kong_fu_xue_tang_jian_cha',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='kong_fu_xue_tang_jian_cha',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='kong_fu_xue_tang_jian_cha',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_kong_fu_xue_tang_jian_cha', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='men_zhen_chu_fang_biao',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='men_zhen_chu_fang_biao',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='men_zhen_chu_fang_biao',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_men_zhen_chu_fang_biao', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='qian_yue_fu_wu',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='qian_yue_fu_wu',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='qian_yue_fu_wu',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_qian_yue_fu_wu', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='shen_qing_kong_fu_xue_tang_jian_cha_fu_wu',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='shen_qing_kong_fu_xue_tang_jian_cha_fu_wu',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='shen_qing_kong_fu_xue_tang_jian_cha_fu_wu',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_shen_qing_kong_fu_xue_tang_jian_cha_fu_wu', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='shu_ye_zhu_she',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='shu_ye_zhu_she',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='shu_ye_zhu_she',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_shu_ye_zhu_she', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='t6301',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='t6301',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='t6301',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_T6301', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='t8901',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='t8901',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='t8901',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_T8901', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='t9001',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='t9001',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='t9001',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_T9001', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='tang_hua_xue_hong_dan_bai_jian_cha_biao',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='tang_hua_xue_hong_dan_bai_jian_cha_biao',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='tang_hua_xue_hong_dan_bai_jian_cha_biao',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_tang_hua_xue_hong_dan_bai_jian_cha_biao', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_cha_ti',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_cha_ti',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_cha_ti',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_tang_niao_bing_cha_ti', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_zhuan_yong_wen_zhen',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_zhuan_yong_wen_zhen',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_zhuan_yong_wen_zhen',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_tang_niao_bing_zhuan_yong_wen_zhen', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_zi_wo_jian_ce',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_zi_wo_jian_ce',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='tang_niao_bing_zi_wo_jian_ce',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_tang_niao_bing_zi_wo_jian_ce', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='xue_ya_jian_ce',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='xue_ya_jian_ce',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='xue_ya_jian_ce',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_xue_ya_jian_ce', to='dictionaries.gender', verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='yao_pin_ji_ben_xin_xi_biao',
            name='boolfield_yao_pin_tong_yong_zi_duan',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='药品通用名'),
        ),
        migrations.AddField(
            model_name='yao_shi_fu_wu',
            name='characterfield_family_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='家庭地址'),
        ),
        migrations.AddField(
            model_name='yao_shi_fu_wu',
            name='datetimefield_date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='出生日期'),
        ),
        migrations.AddField(
            model_name='yao_shi_fu_wu',
            name='relatedfield_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_for_relatedfield_gender_yao_shi_fu_wu', to='dictionaries.gender', verbose_name='性别'),
        ),
    ]
