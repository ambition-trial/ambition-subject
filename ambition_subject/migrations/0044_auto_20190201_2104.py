# Generated by Django 2.1.5 on 2019-02-01 19:04

from django.db import migrations, models
import edc_base.model_validators.date
import edc_base.utils
import edc_model_fields.fields.other_charfield
import edc_protocol.validators


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0043_auto_20190201_0446")]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="reason_missed",
            field=models.CharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If 'missed', provide the reason for the missed visit",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="reason_missed_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=25,
                null=True,
                verbose_name='If the reason for the missed visit is "other", specify',
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="reason_unscheduled_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=25,
                null=True,
                verbose_name='If the reason for the unscheduled visit is "other", specify',
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="report_datetime",
            field=models.DateTimeField(
                default=edc_base.utils.get_utcnow,
                help_text="Date and time of this report",
                validators=[
                    edc_protocol.validators.datetime_not_before_study_start,
                    edc_base.model_validators.date.datetime_not_future,
                ],
                verbose_name="Report date and time",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="reason_missed",
            field=models.CharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If 'missed', provide the reason for the missed visit",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="reason_missed_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=25,
                null=True,
                verbose_name='If the reason for the missed visit is "other", specify',
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="reason_unscheduled_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=25,
                null=True,
                verbose_name='If the reason for the unscheduled visit is "other", specify',
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="report_datetime",
            field=models.DateTimeField(
                default=edc_base.utils.get_utcnow,
                help_text="Date and time of this report",
                validators=[
                    edc_protocol.validators.datetime_not_before_study_start,
                    edc_base.model_validators.date.datetime_not_future,
                ],
                verbose_name="Report date and time",
            ),
        ),
    ]
