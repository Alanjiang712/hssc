# Generated by Django 3.2.6 on 2021-12-01 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customized_forms', '0019_baseform_components'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operandview',
            options={'ordering': ['id'], 'verbose_name': '作业界面', 'verbose_name_plural': '作业界面'},
        ),
    ]
