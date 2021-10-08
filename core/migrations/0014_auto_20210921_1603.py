# Generated by Django 3.2.6 on 2021-09-21 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210921_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='规则名称')),
                ('rule', models.CharField(max_length=255, verbose_name='规则描述')),
            ],
            options={
                'verbose_name': '业务规则表',
                'verbose_name_plural': '业务规则表',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='event_instruction',
            name='rule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.rule', verbose_name='发生规则'),
        ),
    ]