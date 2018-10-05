# Generated by Django 2.1 on 2018-10-01 21:31

import ambition_subject.managers
import ambition_subject.models.subject_requisition
from django.db import migrations
import edc_identifier.managers
import edc_visit_tracking.managers


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0021_auto_20181001_2103'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bloodresult',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='education',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='educationhoh',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='followup',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='lumbarpuncturecsf',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='medicalexpenses',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='medicalexpensestwo',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='microbiology',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='patienthistory',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='pkpdcrf',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='radiology',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='subjectreconsent',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_identifier.managers.SubjectIdentifierManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='subjectrequisition',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', ambition_subject.models.subject_requisition.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='week16',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='week2',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='week4',
            managers=[
                ('on_site', ambition_subject.managers.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
    ]
