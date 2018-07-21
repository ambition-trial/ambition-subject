# Generated by Django 2.0.4 on 2018-05-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0009_auto_20180409_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='fluconazole_dose_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Was the Fluconazole dose given?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='fluconazole_dose_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Was the Fluconazole dose given?'),
        ),
    ]
