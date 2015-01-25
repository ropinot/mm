# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmlog', '0004_activitysheetmodel_machine_down_time_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='component',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_responsible',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_description',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='num_external_operators',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='num_internal_operators',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
