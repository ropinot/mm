# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySheetModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateField()),
                ('entry_time', models.TimeField()),
                ('component', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('internal_responsible', models.CharField(max_length=200)),
                ('num_internal_operators', models.IntegerField()),
                ('internal_intervention_time_days', models.IntegerField()),
                ('internal_intervention_time_hours', models.IntegerField()),
                ('internal_intervention_time_minutes', models.IntegerField()),
                ('internal_intervention_duration', models.IntegerField()),
                ('external_responsible', models.CharField(max_length=200)),
                ('num_external_operators', models.IntegerField()),
                ('external_intervention_time_days', models.IntegerField()),
                ('external_intervention_time_hours', models.IntegerField()),
                ('external_intervention_time_minutes', models.IntegerField()),
                ('external_intervention_duration', models.IntegerField()),
                ('intervention_start_date', models.DateField()),
                ('intervention_start_time', models.TimeField()),
                ('intervention_completion_date', models.DateField()),
                ('intervention_completion_time', models.TimeField()),
                ('machine_down_time_hours', models.IntegerField()),
                ('machine_down_time_days', models.IntegerField()),
                ('machine_down_time', models.IntegerField()),
                ('intervention_description', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityStatusModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponentStatusModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component_status', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExternalMaintenanceCompanyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('responsible', models.CharField(max_length=200)),
                ('num_operators', models.IntegerField()),
                ('intervention_time_days', models.IntegerField()),
                ('intervention_time_hours', models.IntegerField()),
                ('intervention_time_minutes', models.IntegerField()),
                ('intervention_duration', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InterventionTypeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intervention_type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activitysheetmodel',
            name='component_status',
            field=models.ForeignKey(to='mmlog.ComponentStatusModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitysheetmodel',
            name='external_company',
            field=models.ForeignKey(to='mmlog.ExternalMaintenanceCompanyModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitysheetmodel',
            name='intervention_type',
            field=models.ForeignKey(to='mmlog.InterventionTypeModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activitysheetmodel',
            name='status',
            field=models.ForeignKey(to='mmlog.ActivityStatusModel'),
            preserve_default=True,
        ),
    ]
