# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 17:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc_identifier', '0004_auto_20160807_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalIdentifierHistory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, max_length=25)),
                ('identifier_type', models.CharField(max_length=25)),
                ('identifier_prefix', models.CharField(max_length=25, null=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical identifier history',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalIdentifierTracker',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('identifier', models.CharField(db_index=True, max_length=25)),
                ('identifier_string', models.CharField(db_index=True, max_length=50)),
                ('root_number', models.IntegerField(db_index=True)),
                ('counter', models.IntegerField(db_index=True)),
                ('identifier_type', models.CharField(max_length=35)),
                ('device_id', models.CharField(blank=True, max_length=10, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical identifier tracker',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalSubjectIdentifier',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('identifier', models.CharField(db_index=True, editable=False, max_length=36)),
                ('padding', models.IntegerField(default=4, editable=False)),
                ('sequence_number', models.IntegerField()),
                ('device_id', models.IntegerField(default=0)),
                ('is_derived', models.BooleanField(default=False)),
                ('sequence_app_label', models.CharField(default='identifier', editable=False, max_length=50)),
                ('sequence_model_name', models.CharField(default='sequence', editable=False, max_length=50)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical subject identifier',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
    ]
