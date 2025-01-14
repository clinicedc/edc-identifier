# Generated by Django 4.2.7 on 2023-12-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_identifier", "0007_alter_identifiermodel_device_created_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="identifiermodel",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.AlterUniqueTogether(
            name="identifiermodel",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="identifiermodel",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="identifiermodel",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddIndex(
            model_name="identifiermodel",
            index=models.Index(
                fields=["modified", "created"], name="edc_identif_modifie_1b75ca_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="identifiermodel",
            index=models.Index(
                fields=["user_modified", "user_created"],
                name="edc_identif_user_mo_357b53_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="identifiermodel",
            constraint=models.UniqueConstraint(
                fields=("name", "identifier"),
                name="edc_identifier_identifiermodel_name_uniq",
            ),
        ),
    ]
