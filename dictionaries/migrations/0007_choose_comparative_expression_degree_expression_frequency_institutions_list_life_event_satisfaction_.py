# Generated by Django 3.2.6 on 2021-10-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0006_blood_type_contract_signatory_drug_list_education_employee_list_family_relationship_gender_genetic_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '选择',
                'verbose_name_plural': '选择',
            },
        ),
        migrations.CreateModel(
            name='Comparative_expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '比较表达',
                'verbose_name_plural': '比较表达',
            },
        ),
        migrations.CreateModel(
            name='Degree_expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '程度表达',
                'verbose_name_plural': '程度表达',
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '频次',
                'verbose_name_plural': '频次',
            },
        ),
        migrations.CreateModel(
            name='Institutions_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '机构清单',
                'verbose_name_plural': '机构清单',
            },
        ),
        migrations.CreateModel(
            name='Life_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '生活事件',
                'verbose_name_plural': '生活事件',
            },
        ),
        migrations.CreateModel(
            name='Satisfaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '满意度',
                'verbose_name_plural': '满意度',
            },
        ),
        migrations.CreateModel(
            name='Time_period_expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '时段表达',
                'verbose_name_plural': '时段表达',
            },
        ),
    ]
