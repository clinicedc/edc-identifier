# Generated by Django 2.0.1 on 2018-01-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edc_identifier", "0016_auto_20180116_1411")]

    operations = [
        migrations.AddField(
            model_name="identifiermodel",
            name="subject_identifier",
            field=models.CharField(max_length=50, null=True),
        )
    ]
