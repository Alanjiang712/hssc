# Generated by Django 3.2.6 on 2021-09-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_event_instruction_operation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_instruction',
            name='next',
        ),
        migrations.AddField(
            model_name='event_instruction',
            name='next',
            field=models.ManyToManyField(to='core.Operation', verbose_name='下一项作业'),
        ),
    ]