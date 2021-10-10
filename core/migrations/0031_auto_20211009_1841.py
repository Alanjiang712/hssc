# Generated by Django 3.2.6 on 2021-10-09 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0030_auto_20211009_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation_proc',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operation_cid', to=settings.AUTH_USER_MODEL, verbose_name='客户'),
        ),
        migrations.AlterField(
            model_name='operation_proc',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operation', verbose_name='作业'),
        ),
        migrations.AlterField(
            model_name='operation_proc',
            name='ppid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.operation_proc', verbose_name='父进程'),
        ),
        migrations.AlterField(
            model_name='operation_proc',
            name='service_proc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.service_proc', verbose_name='服务'),
        ),
        migrations.AlterField(
            model_name='operation_proc',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operation_uid', to=settings.AUTH_USER_MODEL, verbose_name='操作员'),
        ),
    ]
