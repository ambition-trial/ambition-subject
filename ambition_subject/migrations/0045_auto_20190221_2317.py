# Generated by Django 2.1.5 on 2019-02-21 21:17

from django.db import migrations, models
import edc_model.validators.date


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0044_auto_20190201_2104")]

    operations = [
        migrations.AlterField(
            model_name="historicalweek16",
            name="death_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Leave blank if date is unknown.",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="If deceased, date and time of death",
            ),
        ),
        migrations.AlterField(
            model_name="week16",
            name="death_datetime",
            field=models.DateTimeField(
                blank=True,
                help_text="Leave blank if date is unknown.",
                null=True,
                validators=[edc_model.validators.date.datetime_not_future],
                verbose_name="If deceased, date and time of death",
            ),
        ),
    ]
