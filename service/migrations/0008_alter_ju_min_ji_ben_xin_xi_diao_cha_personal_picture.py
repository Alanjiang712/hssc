# Generated by Django 3.2.6 on 2022-06-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20220602_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ju_min_ji_ben_xin_xi_diao_cha',
            name='personal_picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='个人照片'),
        ),
    ]
