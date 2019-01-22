# Generated by Django 2.1 on 2018-10-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0024_auto_20181009_0545")]

    operations = [
        migrations.AlterField(
            model_name="bloodresult",
            name="action_identifier",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="bloodresult",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bloodresult",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresult",
            name="action_identifier",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalbloodresult",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresult",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectreconsent",
            name="action_identifier",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalsubjectreconsent",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectreconsent",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="subjectreconsent",
            name="action_identifier",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="subjectreconsent",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="subjectreconsent",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
    ]
