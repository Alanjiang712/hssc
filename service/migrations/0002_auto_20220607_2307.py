# Generated by Django 3.2.6 on 2022-06-07 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='li_pei_shen_qing_chong_shen',
            options={'verbose_name': '重新申请理赔', 'verbose_name_plural': '重新申请理赔'},
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_bao_dan_hao',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_bao_xian_you_xiao_qi',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_bao_xian_ze_ren',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_lian_xi_dian_hua',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_xu_hao',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='boolfield_zheng_jian_lei_xing',
        ),
        migrations.RemoveField(
            model_name='fen_zhen_que_ren',
            name='characterhssc_identification_number',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_bao_dan_hao',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_bao_xian_you_xiao_qi',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_bao_xian_ze_ren',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_lian_xi_dian_hua',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_xu_hao',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='boolfield_zheng_jian_lei_xing',
        ),
        migrations.RemoveField(
            model_name='yu_yue_que_ren',
            name='characterhssc_identification_number',
        ),
    ]
