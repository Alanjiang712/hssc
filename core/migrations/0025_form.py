# Generated by Django 3.2.6 on 2021-10-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_event_instructions_params'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='表单名')),
                ('label', models.CharField(max_length=255, verbose_name='显示名称')),
            ],
            options={
                'verbose_name': '表单',
                'verbose_name_plural': '表单',
                'ordering': ['id'],
            },
        ),
    ]
