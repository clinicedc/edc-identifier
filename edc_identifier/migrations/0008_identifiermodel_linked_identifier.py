# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_identifier", "0007_auto_20161204_2227")]

    operations = [
        migrations.AddField(
            model_name="identifiermodel",
            name="linked_identifier",
            field=models.CharField(max_length=50, null=True),
        )
    ]
