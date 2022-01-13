# Generated by Django 3.2.6 on 2022-01-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20220112_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergies_history',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='basic_personal_information',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='blood_pressure_monitoring',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='doctor_login',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='doctor_registry',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='dorsal_artery_pulsation_examination',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='family_history_of_illness',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='fundus_examination',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='history_of_blood_transfusion',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='history_of_infectious_diseases',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='history_of_surgery',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='history_of_trauma',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='lower_extremity_edema_examination',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='major_life_events',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='medical_history',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='out_of_hospital_self_report_survey',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='personal_adaptability_assessment',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='personal_comprehensive_psychological_quality_survey',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='personal_health_assessment',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='personal_health_behavior_survey',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='physical_examination',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='physical_examination_athletic_ability',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='physical_examination_hearing',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='physical_examination_oral_cavity',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='physical_examination_vision',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='social_environment_assessment',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='user_registry',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='vital_signs_check',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='slug'),
        ),
    ]
