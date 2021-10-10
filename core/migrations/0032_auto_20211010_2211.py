# Generated by Django 3.2.6 on 2021-10-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20211009_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='事件名'),
        ),
        migrations.AlterField(
            model_name='operation_proc',
            name='entry',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True, verbose_name='作业入口'),
        ),
    ]
