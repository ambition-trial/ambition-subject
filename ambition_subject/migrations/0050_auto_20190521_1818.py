# Generated by Django 2.2 on 2019-05-21 16:18

import django.core.validators
from django.db import migrations, models
import edc_model.validators.date
import edc_model_fields.fields.date_estimated
import edc_model_fields.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_lists', '0004_arvregimens'),
        ('ambition_subject', '0049_auto_20190517_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_date',
            field=models.DateField(blank=True, null=True, validators=[edc_model.validators.date.date_not_future], verbose_name='If Yes, when was their current or most recent ART regimen started?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_date_estimated',
            field=edc_model_fields.fields.date_estimated.IsDateEstimatedFieldNa(choices=[('N/A', 'Not applicable'), ('not_estimated', 'No.'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], default='N/A', help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, verbose_name="Is the subject's ARV date estimated?"),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_decision',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('ART continued', 'ART continued'), ('ART stopped', 'ART stopped')], default='N/A', max_length=25, verbose_name='What decision was made at admission regarding their current ART regimen?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_defaulted_date',
            field=models.DateField(blank=True, null=True, validators=[edc_model.validators.date.date_not_future], verbose_name='If the patient has defaulted, on what date did they default from their most recent ART regimen?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_defaulted_estimated',
            field=edc_model_fields.fields.date_estimated.IsDateEstimatedFieldNa(choices=[('N/A', 'Not applicable'), ('not_estimated', 'No.'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], default='N/A', help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, verbose_name='Is this ART date estimated?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_is_adherent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='If the patient is currently on ART, are they adherent to their current ART regimen?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_is_defaulted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text="'Default' means no ART for at least one month", max_length=5, verbose_name='Has the patient now defaulted from their ART regimen?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='current_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='has_switched_regimen',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Has the patient ever switched ART regimen?'),
        ),
        migrations.AddField(
            model_name='historicalpatienthistory',
            name='initial_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_date',
            field=models.DateField(blank=True, null=True, validators=[edc_model.validators.date.date_not_future], verbose_name='If Yes, when was their current or most recent ART regimen started?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_date_estimated',
            field=edc_model_fields.fields.date_estimated.IsDateEstimatedFieldNa(choices=[('N/A', 'Not applicable'), ('not_estimated', 'No.'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], default='N/A', help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, verbose_name="Is the subject's ARV date estimated?"),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_decision',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('ART continued', 'ART continued'), ('ART stopped', 'ART stopped')], default='N/A', max_length=25, verbose_name='What decision was made at admission regarding their current ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_defaulted_date',
            field=models.DateField(blank=True, null=True, validators=[edc_model.validators.date.date_not_future], verbose_name='If the patient has defaulted, on what date did they default from their most recent ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_defaulted_estimated',
            field=edc_model_fields.fields.date_estimated.IsDateEstimatedFieldNa(choices=[('N/A', 'Not applicable'), ('not_estimated', 'No.'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], default='N/A', help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, verbose_name='Is this ART date estimated?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_is_adherent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='If the patient is currently on ART, are they adherent to their current ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_is_defaulted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text="'Default' means no ART for at least one month", max_length=5, verbose_name='Has the patient now defaulted from their ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_regimen',
            field=models.ManyToManyField(related_name='current_arv', to='ambition_lists.ArvRegimens', verbose_name='If Yes, what is their current or most recent ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='current_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='has_switched_regimen',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Has the patient ever switched ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='initial_arv_regimen',
            field=models.ManyToManyField(related_name='first_arv', to='ambition_lists.ArvRegimens', verbose_name='If YES, which drugs were prescribed for their first ART regimen?'),
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='initial_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='arv_date',
            field=models.DateField(blank=True, null=True, validators=[edc_model.validators.date.date_not_future], verbose_name='If YES, when did the patient start ART for the first time.'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='first_arv_regimen',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('TDF_3TC_FTC_with_EFV_or_NVP', 'TDF + 3TC/FTC + either EFV or NVP or DTG'), ('AZT_3TC_with_EFV_NVP_or_DTG', 'AZT+3TC+ either EFV or NVP or DTG'), ('OTHER', 'Other')], default='N/A', editable=False, max_length=50, verbose_name='If YES, which drugs were prescribed for their first ART regimen?'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='first_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, editable=False, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='first_line_choice',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('EFV', 'EFV'), ('DTG', 'DTG'), ('NVP', 'NVP'), ('OTHER', 'Other')], default='N/A', editable=False, max_length=5, verbose_name='If first line:'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='last_dose',
            field=models.IntegerField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='If no tablets taken this month, how many months since the last dose taken?'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='patient_adherence',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', editable=False, max_length=5, verbose_name='Is the patient reportedly adherent?'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='second_arv_regimen',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r', 'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'), ('AZT_3TC_with_ATZ_r_or_Lopinavir_r', 'AZT +3TC + either ATZ/r or Lopinavir/r'), ('OTHER', 'Other'), ('QUESTION_RETIRED', 'QUESTION_RETIRED')], default='QUESTION_RETIRED', editable=False, max_length=50, verbose_name='Second line ARV regimen'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='second_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, editable=False, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='taking_arv',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='If NO, has the patient ever been on ART?'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='arv_date',
            field=models.DateField(blank=True, null=True, validators=[edc_model.validators.date.date_not_future], verbose_name='If YES, when did the patient start ART for the first time.'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='first_arv_regimen',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('TDF_3TC_FTC_with_EFV_or_NVP', 'TDF + 3TC/FTC + either EFV or NVP or DTG'), ('AZT_3TC_with_EFV_NVP_or_DTG', 'AZT+3TC+ either EFV or NVP or DTG'), ('OTHER', 'Other')], default='N/A', editable=False, max_length=50, verbose_name='If YES, which drugs were prescribed for their first ART regimen?'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='first_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, editable=False, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='first_line_choice',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('EFV', 'EFV'), ('DTG', 'DTG'), ('NVP', 'NVP'), ('OTHER', 'Other')], default='N/A', editable=False, max_length=5, verbose_name='If first line:'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='last_dose',
            field=models.IntegerField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='If no tablets taken this month, how many months since the last dose taken?'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='patient_adherence',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', editable=False, max_length=5, verbose_name='Is the patient reportedly adherent?'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='second_arv_regimen',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r', 'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'), ('AZT_3TC_with_ATZ_r_or_Lopinavir_r', 'AZT +3TC + either ATZ/r or Lopinavir/r'), ('OTHER', 'Other'), ('QUESTION_RETIRED', 'QUESTION_RETIRED')], default='QUESTION_RETIRED', editable=False, max_length=50, verbose_name='Second line ARV regimen'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='second_arv_regimen_other',
            field=edc_model_fields.fields.other_charfield.OtherCharField(blank=True, editable=False, max_length=35, null=True, verbose_name='If Other, specify ...'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='taking_arv',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='If NO, has the patient ever been on ART?'),
        ),
    ]
