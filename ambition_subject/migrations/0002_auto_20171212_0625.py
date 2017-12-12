# Generated by Django 2.0 on 2017-12-12 04:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodresult',
            name='vl',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Viral Load'),
        ),
        migrations.AddField(
            model_name='bloodresult',
            name='vl_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='bloodresult',
            name='vl_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='bloodresult',
            name='vl_units',
            field=models.CharField(blank=True, choices=[('copies/mL', 'copies/mL')], default='copies/mL', max_length=10, null=True, verbose_name='units'),
        ),
        migrations.AddField(
            model_name='historicalbloodresult',
            name='vl',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Viral Load'),
        ),
        migrations.AddField(
            model_name='historicalbloodresult',
            name='vl_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6, null=True, verbose_name='abnormal'),
        ),
        migrations.AddField(
            model_name='historicalbloodresult',
            name='vl_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AddField(
            model_name='historicalbloodresult',
            name='vl_units',
            field=models.CharField(blank=True, choices=[('copies/mL', 'copies/mL')], default='copies/mL', max_length=10, null=True, verbose_name='units'),
        ),
    ]