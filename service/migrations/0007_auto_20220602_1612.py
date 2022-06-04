# Generated by Django 3.2.6 on 2022-06-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_ju_min_ji_ben_xin_xi_diao_cha_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ju_min_ji_ben_xin_xi_diao_cha',
            name='test',
        ),
        migrations.AddField(
            model_name='ju_min_ji_ben_xin_xi_diao_cha',
            name='personal_picture',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='个人照片'),
        ),
    ]
