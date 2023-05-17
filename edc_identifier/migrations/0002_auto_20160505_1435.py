# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_identifier", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="identifiertracker",
            name="hostname_created",
            field=models.CharField(
                default="mac2-2.local",
                editable=False,
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="sequence",
            name="hostname_created",
            field=models.CharField(
                default="mac2-2.local",
                editable=False,
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="subjectidentifier",
            name="hostname_created",
            field=models.CharField(
                default="mac2-2.local",
                editable=False,
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
    ]
