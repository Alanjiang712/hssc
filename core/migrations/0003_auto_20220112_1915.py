# Generated by Django 3.2.6 on 2022-01-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_operation_proc_form_slugs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_proc',
            name='user',
        ),
        migrations.AddField(
            model_name='service_proc',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_uid', to='core.staff', verbose_name='服务专员'),
        ),
        migrations.AlterField(
            model_name='service_proc',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_cid', to='core.customer', verbose_name='客户'),
        ),
    ]
