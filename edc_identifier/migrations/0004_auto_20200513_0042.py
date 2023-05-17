# Generated by Django 3.0.4 on 2020-05-12 21:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edc_identifier", "0003_auto_20191024_1000"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="identifiermodel",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ["sequence_number"],
            },
        ),
    ]
