# Generated by Django 3.2.6 on 2021-11-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customized_forms', '0018_auto_20211129_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseform',
            name='components',
            field=models.ManyToManyField(to='customized_forms.Component', verbose_name='组件清单'),
        ),
    ]
