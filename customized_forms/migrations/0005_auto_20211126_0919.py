# Generated by Django 3.2.6 on 2021-11-26 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('customized_forms', '0004_alter_component_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('app_label', 'customized_forms'), models.Q(('model', 'characterfield'), ('model', 'numberfield'), ('model', 'dtfield'), ('model', 'choicefield'), ('model', 'relatedfield'), ('model', 'computefield'), _connector='OR')), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='operandview',
            name='axis_field',
            field=models.CharField(choices=[('customer', '客户'), ('staff', '员工'), ('medicine', '药品'), ('device', '设备')], default='customer', max_length=255, verbose_name='业务主键'),
        ),
    ]