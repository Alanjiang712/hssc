# Generated by Django 3.2.6 on 2021-10-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_rule_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='fields_list',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='表单字段'),
        ),
    ]
