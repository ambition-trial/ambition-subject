# Generated by Django 2.1 on 2018-08-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0015_auto_20180810_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectconsent',
            name='screening_datetime',
            field=models.DateTimeField(editable=False, null=True, verbose_name='Screening datetime'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='screening_datetime',
            field=models.DateTimeField(editable=False, null=True, verbose_name='Screening datetime'),
        ),
    ]
