# Generated by Django 3.2.6 on 2021-08-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionaries', '0003_auto_20210830_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '血型',
                'verbose_name_plural': '血型',
            },
        ),
        migrations.CreateModel(
            name='Contract_signatory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '合同签约户',
                'verbose_name_plural': '合同签约户',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '文化程度',
                'verbose_name_plural': '文化程度',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '性别',
                'verbose_name_plural': '性别',
            },
        ),
        migrations.CreateModel(
            name='Marital_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '婚姻状况',
                'verbose_name_plural': '婚姻状况',
            },
        ),
        migrations.CreateModel(
            name='Medical_expenses_burden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '医疗费用负担',
                'verbose_name_plural': '医疗费用负担',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '民族',
                'verbose_name_plural': '民族',
            },
        ),
        migrations.CreateModel(
            name='Occupational_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '职业状况',
                'verbose_name_plural': '职业状况',
            },
        ),
        migrations.CreateModel(
            name='Relationship_with_the_head_of_household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '与户主关系',
                'verbose_name_plural': '与户主关系',
            },
        ),
        migrations.CreateModel(
            name='Service_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '服务角色',
                'verbose_name_plural': '服务角色',
            },
        ),
        migrations.CreateModel(
            name='Type_of_residence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='名称')),
                ('score', models.SmallIntegerField(blank=True, null=True, verbose_name='分值')),
            ],
            options={
                'verbose_name': '居住类型',
                'verbose_name_plural': '居住类型',
            },
        ),
    ]