# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mmlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysheet',
            name='component',
            field=models.CharField(default=datetime.datetime(2014, 10, 24, 20, 44, 33, 453197, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitysheet',
            name='description',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitysheet',
            name='entry_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
