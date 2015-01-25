# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmlog', '0005_auto_20141028_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='component',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='component_status',
            field=models.ForeignKey(blank=True, to='mmlog.ComponentStatusModel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='entry_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='entry_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_company',
            field=models.ForeignKey(blank=True, to='mmlog.ExternalMaintenanceCompanyModel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_intervention_duration',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_intervention_time_days',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_intervention_time_hours',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_intervention_time_minutes',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_responsible',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='internal_intervention_duration',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='internal_intervention_time_days',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='internal_intervention_time_hours',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='internal_intervention_time_minutes',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='internal_responsible',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_completion_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_completion_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_description',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_start_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_start_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_type',
            field=models.ForeignKey(blank=True, to='mmlog.InterventionTypeModel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='machine_down_time',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='machine_down_time_days',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='machine_down_time_hours',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='machine_down_time_minutes',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='num_external_operators',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='num_internal_operators',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='status',
            field=models.ForeignKey(blank=True, to='mmlog.ActivityStatusModel', null=True),
            preserve_default=True,
        ),
    ]
