# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmlog', '0002_auto_20141025_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='component_status',
            field=models.ForeignKey(to='mmlog.ComponentStatusModel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='external_company',
            field=models.ForeignKey(to='mmlog.ExternalMaintenanceCompanyModel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='intervention_type',
            field=models.ForeignKey(to='mmlog.InterventionTypeModel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activitysheetmodel',
            name='status',
            field=models.ForeignKey(to='mmlog.ActivityStatusModel', null=True),
            preserve_default=True,
        ),
    ]
