# Generated by Django 2.1.2 on 2018-10-24 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0029_auto_20181024_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amphotericinmisseddoses',
            old_name='ampho_day_missed',
            new_name='day_missed',
        ),
        migrations.RenameField(
            model_name='amphotericinmisseddoses',
            old_name='ampho_missed_reason',
            new_name='missed_reason',
        ),
        migrations.RenameField(
            model_name='historicalamphotericinmisseddoses',
            old_name='ampho_day_missed',
            new_name='day_missed',
        ),
        migrations.RenameField(
            model_name='historicalamphotericinmisseddoses',
            old_name='ampho_missed_reason',
            new_name='missed_reason',
        ),
        migrations.AlterUniqueTogether(
            name='amphotericinmisseddoses',
            unique_together={('week2', 'day_missed', 'missed_reason')},
        ),
    ]
