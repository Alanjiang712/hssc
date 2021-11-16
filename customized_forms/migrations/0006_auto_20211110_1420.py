# Generated by Django 3.2.6 on 2021-11-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20211102_2022'),
        ('customized_forms', '0005_auto_20211110_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operand_form',
            name='inquire_forms',
            field=models.ManyToManyField(related_name='inquire_forms', to='core.Form', verbose_name='查询子表单'),
        ),
        migrations.AlterField(
            model_name='operand_form',
            name='mutate_forms',
            field=models.ManyToManyField(related_name='mutate_forms', to='core.Form', verbose_name='变更子表单'),
        ),
    ]