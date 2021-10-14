# Generated by Django 3.2.6 on 2021-10-14 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icpc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0014_auto_20211010_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vital_signs_check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_temperature', models.SmallIntegerField(blank=True, null=True, verbose_name='体温')),
                ('pulse', models.SmallIntegerField(blank=True, null=True, verbose_name='脉搏')),
                ('respiratory_rate', models.SmallIntegerField(blank=True, null=True, verbose_name='呼吸频率')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vital_signs_check_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vital_signs_check_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '生命体征检查',
                'verbose_name_plural': '生命体征检查',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_eye_vision', models.CharField(blank=True, max_length=60, null=True, verbose_name='左眼视力')),
                ('right_eye_vision', models.CharField(blank=True, max_length=60, null=True, verbose_name='右眼视力')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_vision_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_vision_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体视力',
                'verbose_name_plural': '查体视力',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_spine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_spine_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_spine_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体脊柱',
                'verbose_name_plural': '查体脊柱',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_skin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_skin_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('skin', models.ForeignKey(db_column='icpc_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='icpc.icpc3_symptoms_and_problems', verbose_name='皮肤')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_skin_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体皮肤',
                'verbose_name_plural': '查体皮肤',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_sclera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_sclera_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('sclera', models.ForeignKey(db_column='icpc_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='icpc.icpc3_symptoms_and_problems', verbose_name='巩膜')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_sclera_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体巩膜',
                'verbose_name_plural': '查体巩膜',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_oral_cavity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lips', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='口唇')),
                ('dentition', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='齿列')),
                ('pharynx', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='咽部')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_oral_cavity_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_oral_cavity_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体口腔',
                'verbose_name_plural': '查体口腔',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_lymph_nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_lymph_nodes_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('lymph_nodes', models.ForeignKey(db_column='icpc_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='icpc.icpc3_symptoms_and_problems', verbose_name='淋巴结')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_lymph_nodes_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体淋巴结',
                'verbose_name_plural': '查体淋巴结',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_lungs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrel_chest', models.CharField(blank=True, choices=[('0', '不确定'), ('1', '是'), ('2', '否'), ('3', '无'), ('4', '有')], max_length=60, null=True, verbose_name='桶状胸')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_lungs_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_lungs_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体肺部',
                'verbose_name_plural': '查体肺部',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_limbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_limbs_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_limbs_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体四肢',
                'verbose_name_plural': '查体四肢',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_hearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_ear_hearing', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='左耳听力')),
                ('rightearhearing', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='右耳听力')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_hearing_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_hearing_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体听力',
                'verbose_name_plural': '查体听力',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_diabetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fundus', models.CharField(blank=True, choices=[('0', '不确定'), ('1', '是'), ('2', '否'), ('3', '无'), ('4', '有')], max_length=60, null=True, verbose_name='眼底')),
                ('lower_extremity_edema', models.CharField(blank=True, choices=[('0', '不确定'), ('1', '是'), ('2', '否'), ('3', '无'), ('4', '有')], max_length=60, null=True, verbose_name='下肢水肿')),
                ('zbdm', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='足背动脉搏动')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_diabetes_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_diabetes_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体糖尿病',
                'verbose_name_plural': '查体糖尿病',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_athletic_ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athletic_ability', models.CharField(blank=True, choices=[], max_length=60, null=True, verbose_name='运动能力')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_athletic_ability_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_athletic_ability_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体运动能力',
                'verbose_name_plural': '查体运动能力',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination_abdomen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenderness', models.CharField(blank=True, choices=[('0', '不确定'), ('1', '是'), ('2', '否'), ('3', '无'), ('4', '有')], max_length=60, null=True, verbose_name='压痛')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_abdomen_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_abdomen_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '查体腹部',
                'verbose_name_plural': '查体腹部',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Physical_examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hight', models.SmallIntegerField(blank=True, null=True, verbose_name='身高')),
                ('weight', models.SmallIntegerField(blank=True, null=True, verbose_name='体重')),
                ('body_mass_index', models.SmallIntegerField(blank=True, null=True, verbose_name='体质指数')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='physical_examination_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '体格检查',
                'verbose_name_plural': '体格检查',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Blood_pressure_monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic_blood_pressure', models.SmallIntegerField(blank=True, null=True, verbose_name='收缩压')),
                ('diastolic_blood_pressure', models.SmallIntegerField(blank=True, null=True, verbose_name='舒张压')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blood_pressure_monitoring_cid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blood_pressure_monitoring_uid', to=settings.AUTH_USER_MODEL, verbose_name='作业人员')),
            ],
            options={
                'verbose_name': '血压监测',
                'verbose_name_plural': '血压监测',
                'ordering': [],
            },
        ),
    ]