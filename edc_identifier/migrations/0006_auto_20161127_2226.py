# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django_revision.revision_field
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
import edc_model_fields.fields.uuid_auto_field
import edc_utils


class Migration(migrations.Migration):

    dependencies = [
        (
            "edc_identifier",
            "0005_historicalidentifierhistory_historicalidentifiertracker_historicalsubjectidentifier",
        )
    ]

    operations = [
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="hostname_created",
            field=models.CharField(
                default="mac2-2.local",
                editable=False,
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="hostname_modified",
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                editable=False,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="revision",
            field=django_revision.revision_field.RevisionField(
                blank=True,
                editable=False,
                help_text="System field. Git repository tag:branch:commit.",
                max_length=75,
                null=True,
                verbose_name="Revision",
            ),
        ),
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="user_created",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, editable=False, max_length=50, verbose_name="user created"
            ),
        ),
        migrations.AddField(
            model_name="historicalidentifierhistory",
            name="user_modified",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, editable=False, max_length=50, verbose_name="user modified"
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="hostname_created",
            field=models.CharField(
                default="mac2-2.local",
                editable=False,
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="hostname_modified",
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                editable=False,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="revision",
            field=django_revision.revision_field.RevisionField(
                blank=True,
                editable=False,
                help_text="System field. Git repository tag:branch:commit.",
                max_length=75,
                null=True,
                verbose_name="Revision",
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="user_created",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, editable=False, max_length=50, verbose_name="user created"
            ),
        ),
        migrations.AddField(
            model_name="identifierhistory",
            name="user_modified",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, editable=False, max_length=50, verbose_name="user modified"
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentifierhistory",
            name="history_id",
            field=edc_model_fields.fields.uuid_auto_field.UUIDAutoField(
                primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentifierhistory",
            name="id",
            field=edc_model_fields.fields.uuid_auto_field.UUIDAutoField(
                blank=True,
                db_index=True,
                editable=False,
                help_text="System auto field. UUID primary key.",
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentifiertracker",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalidentifiertracker",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectidentifier",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectidentifier",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="identifierhistory",
            name="id",
            field=edc_model_fields.fields.uuid_auto_field.UUIDAutoField(
                blank=True,
                editable=False,
                help_text="System auto field. UUID primary key.",
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="identifiertracker",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="identifiertracker",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="sequence",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="sequence",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="subjectidentifier",
            name="created",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
        migrations.AlterField(
            model_name="subjectidentifier",
            name="modified",
            field=models.DateTimeField(
                default=edc_utils.date.get_utcnow, editable=False
            ),
        ),
    ]
