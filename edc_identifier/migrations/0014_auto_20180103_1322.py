# Generated by Django 2.0 on 2018-01-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_identifier", "0013_auto_20171230_1316")]

    operations = [
        migrations.AlterField(
            model_name="identifiermodel", name="device_id", field=models.IntegerField()
        ),
        migrations.AlterField(
            model_name="identifiermodel",
            name="identifier_type",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="identifiermodel",
            name="model",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="identifiermodel",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="identifiermodel",
            name="protocol_number",
            field=models.CharField(max_length=25),
        ),
    ]
