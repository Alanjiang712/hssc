# Generated by Django 3.2.6 on 2021-09-21 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_event_instruction_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_instruction',
            name='icpc',
        ),
        migrations.AddField(
            model_name='event_instruction',
            name='rule',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='发生规则'),
        ),
        migrations.AlterField(
            model_name='event_instruction',
            name='next',
            field=models.ManyToManyField(to='core.Operation', verbose_name='后续作业'),
        ),
        migrations.AlterField(
            model_name='event_instruction',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_oid', to='core.operation', verbose_name='作业'),
        ),
    ]
