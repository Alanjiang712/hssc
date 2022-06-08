# Generated by Django 3.2.6 on 2022-06-08 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('service', '0003_auto_20220608_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chong_xin_yu_yue_an_pai',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_chong_xin_yu_yue_an_pai', to='core.staff', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='fen_zhen_que_ren',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_fen_zhen_que_ren', to='core.staff', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='yu_yue_an_pai',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_yu_yue_an_pai', to='core.staff', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='yu_yue_que_ren',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_yu_yue_que_ren', to='core.staff', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='yu_yue_zi_xun',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_yu_yue_zi_xun', to='core.staff', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='zhen_suo_yu_yue',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_zhen_suo_yu_yue', to='core.staff', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='zhi_yuan_ji_ben_xin_xi_biao',
            name='relatedfield_affiliation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution_for_relatedfield_affiliation_zhi_yuan_ji_ben_xin_xi_biao', to='core.institution', verbose_name='所属机构'),
        ),
    ]
