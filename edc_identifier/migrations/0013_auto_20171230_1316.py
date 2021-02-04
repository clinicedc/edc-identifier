# Generated by Django 2.0 on 2017-12-30 13:16

import django.contrib.sites.managers
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("edc_identifier", "0012_auto_20171116_1606"),
    ]

    operations = [
        migrations.RemoveField(model_name="historicalidentifierhistory", name="history_user"),
        migrations.RemoveField(model_name="historicalidentifiertracker", name="history_user"),
        migrations.RemoveField(model_name="historicalsubjectidentifier", name="history_user"),
        migrations.DeleteModel(name="IdentifierHistory"),
        migrations.DeleteModel(name="IdentifierTracker"),
        migrations.DeleteModel(name="Sequence"),
        migrations.DeleteModel(name="SubjectIdentifier"),
        migrations.AlterModelManagers(
            name="identifiermodel",
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.RenameField(
            model_name="identifiermodel",
            old_name="subject_type",
            new_name="identifier_type",
        ),
        migrations.RemoveField(model_name="identifiermodel", name="study_site"),
        migrations.AddField(
            model_name="identifiermodel",
            name="identifier_prefix",
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name="identifiermodel",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="sites.Site",
            ),
        ),
        migrations.AlterField(
            model_name="identifiermodel",
            name="sequence_number",
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(name="HistoricalIdentifierHistory"),
        migrations.DeleteModel(name="HistoricalIdentifierTracker"),
        migrations.DeleteModel(name="HistoricalSubjectIdentifier"),
    ]
