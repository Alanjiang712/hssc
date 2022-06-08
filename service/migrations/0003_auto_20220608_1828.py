# Generated by Django 3.2.6 on 2022-06-08 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20220608_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yu_yue_an_pai',
            options={'verbose_name': '平台预约安排', 'verbose_name_plural': '平台预约安排'},
        ),
        migrations.RemoveField(
            model_name='bao_xian_yong_hu_zhu_ce',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='bao_xian_yong_hu_zhu_ce',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='bao_xian_yong_hu_zhu_ce',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='bao_xian_yong_hu_zhu_ce',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='chong_xin_yu_yue_an_pai',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='chong_xin_yu_yue_an_pai',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='chong_xin_yu_yue_an_pai',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='chong_xin_yu_yue_an_pai',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='li_pei_shen_qing_chong_shen',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='li_pei_shen_qing_chong_shen',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='li_pei_shen_qing_fu_wu',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='li_pei_shen_qing_fu_wu',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='li_pei_shen_qing_shu_shen_he',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='li_pei_shen_qing_shu_shen_he',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='man_yi_du_diao_cha',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='man_yi_du_diao_cha',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='man_yi_du_diao_cha',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='man_yi_du_diao_cha',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu_hui_zong',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu_hui_zong',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu_hui_zong',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='men_zhen_ji_lu_hui_zong',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='ti_jiao_he_bao_zi_liao',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='ti_jiao_he_bao_zi_liao',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='yu_yue_an_pai',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='yu_yue_an_pai',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='yu_yue_an_pai',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='yu_yue_an_pai',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='yu_yue_tong_zhi',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='yu_yue_tong_zhi',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='yu_yue_tong_zhi',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='yu_yue_tong_zhi',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='yu_yue_zi_xun',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='yu_yue_zi_xun',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='yu_yue_zi_xun',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='yu_yue_zi_xun',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='zhen_hou_sui_fang',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='zhen_hou_sui_fang',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='zhen_hou_sui_fang',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='zhen_hou_sui_fang',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='zhen_jian_sui_fang',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='zhen_jian_sui_fang',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='zhen_jian_sui_fang',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='zhen_jian_sui_fang',
            name='datetimefield_date_of_birth',
        ),
        migrations.RemoveField(
            model_name='zhen_suo_yu_yue',
            name='boolfield_chang_zhu_di_zhi',
        ),
        migrations.RemoveField(
            model_name='zhen_suo_yu_yue',
            name='characterfield_gender',
        ),
        migrations.RemoveField(
            model_name='zhen_suo_yu_yue',
            name='characterfield_name',
        ),
        migrations.RemoveField(
            model_name='zhen_suo_yu_yue',
            name='datetimefield_date_of_birth',
        ),
        migrations.AlterField(
            model_name='chong_xin_yu_yue_an_pai',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhi_yuan_ji_ben_xin_xi_biao_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_chong_xin_yu_yue_an_pai', to='service.zhi_yuan_ji_ben_xin_xi_biao', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='fen_zhen_que_ren',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhi_yuan_ji_ben_xin_xi_biao_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_fen_zhen_que_ren', to='service.zhi_yuan_ji_ben_xin_xi_biao', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='yu_yue_an_pai',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhi_yuan_ji_ben_xin_xi_biao_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_yu_yue_an_pai', to='service.zhi_yuan_ji_ben_xin_xi_biao', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='yu_yue_que_ren',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhi_yuan_ji_ben_xin_xi_biao_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_yu_yue_que_ren', to='service.zhi_yuan_ji_ben_xin_xi_biao', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='yu_yue_zi_xun',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhi_yuan_ji_ben_xin_xi_biao_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_yu_yue_zi_xun', to='service.zhi_yuan_ji_ben_xin_xi_biao', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='zhen_suo_yu_yue',
            name='boolfield_jiu_zhen_ji_gou_ze_ren_ren',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhi_yuan_ji_ben_xin_xi_biao_for_boolfield_jiu_zhen_ji_gou_ze_ren_ren_zhen_suo_yu_yue', to='service.zhi_yuan_ji_ben_xin_xi_biao', verbose_name='就诊机构责任人'),
        ),
        migrations.AlterField(
            model_name='zhi_yuan_ji_ben_xin_xi_biao',
            name='relatedfield_affiliation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ji_gou_ji_ben_xin_xi_biao_for_relatedfield_affiliation_zhi_yuan_ji_ben_xin_xi_biao', to='service.ji_gou_ji_ben_xin_xi_biao', verbose_name='所属机构'),
        ),
    ]
