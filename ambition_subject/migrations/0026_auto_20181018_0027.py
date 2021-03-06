# Generated by Django 2.1 on 2018-10-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0025_auto_20181010_2116")]

    operations = [
        migrations.AddField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_four",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;4</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_one",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;1</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_three",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;3</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_two",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;2</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="pkpdcrf",
            name="flucytosine_dose_four",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;4</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="pkpdcrf",
            name="flucytosine_dose_one",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;1</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="pkpdcrf",
            name="flucytosine_dose_three",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;3</u> dose?",
            ),
        ),
        migrations.AddField(
            model_name="pkpdcrf",
            name="flucytosine_dose_two",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                verbose_name="Flucytosine <u>DOSE&nbsp;2</u> dose?",
            ),
        ),
        migrations.AlterField(
            model_name="historicallumbarpuncturecsf",
            name="csf_protein",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Units in g/L",
                max_digits=4,
                null=True,
                verbose_name="CSF protein:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose",
            field=models.IntegerField(
                blank=True,
                help_text="Total dose. Units in mg",
                null=True,
                verbose_name="Flucytosine dose?",
            ),
        ),
        migrations.AlterField(
            model_name="lumbarpuncturecsf",
            name="csf_protein",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Units in g/L",
                max_digits=4,
                null=True,
                verbose_name="CSF protein:",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose",
            field=models.IntegerField(
                blank=True,
                help_text="Total dose. Units in mg",
                null=True,
                verbose_name="Flucytosine dose?",
            ),
        ),
    ]
