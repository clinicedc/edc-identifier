# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 09:38
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_identifier", "0002_auto_20160505_1435")]

    operations = [
        migrations.AlterField(
            model_name="identifiertracker",
            name="id",
            field=models.UUIDField(
                blank=True,
                default=uuid.uuid4,
                editable=False,
                help_text="System auto field. UUID primary key.",
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="subjectidentifier",
            name="id",
            field=models.UUIDField(
                blank=True,
                default=uuid.uuid4,
                editable=False,
                help_text="System auto field. UUID primary key.",
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
