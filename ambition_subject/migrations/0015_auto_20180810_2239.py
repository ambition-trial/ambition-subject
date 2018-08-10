# Generated by Django 2.1 on 2018-08-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0014_auto_20180809_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectconsent',
            name='screening_identifier',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Screening identifier'),
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='screening_identifier',
            field=models.CharField(max_length=50, unique=True, verbose_name='Screening identifier'),
        ),
    ]
