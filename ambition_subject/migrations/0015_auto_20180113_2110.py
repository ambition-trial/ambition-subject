# Generated by Django 2.0.1 on 2018-01-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0014_auto_20180113_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectrequisition',
            name='panel_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subjectrequisition',
            name='panel_name',
            field=models.CharField(max_length=50),
        ),
    ]
