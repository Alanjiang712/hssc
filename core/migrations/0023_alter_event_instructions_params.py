# Generated by Django 3.2.6 on 2021-10-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20211007_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_instructions',
            name='params',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='创建作业'),
        ),
    ]
