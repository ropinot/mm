# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmlog', '0003_auto_20141025_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysheetmodel',
            name='machine_down_time_minutes',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
