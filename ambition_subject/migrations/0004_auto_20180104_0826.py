# Generated by Django 2.0 on 2018-01-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0003_auto_20180104_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectconsent',
            name='report_datetime',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='report_datetime',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalsubjectconsent',
            name='sid',
            field=models.CharField(blank=True, editable=False, help_text='Used for randomization against a prepared rando-list.', max_length=15, null=True, verbose_name='SID'),
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='sid',
            field=models.CharField(blank=True, editable=False, help_text='Used for randomization against a prepared rando-list.', max_length=15, null=True, verbose_name='SID'),
        ),
    ]