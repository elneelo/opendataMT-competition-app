# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0036_auto_20150320_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 20, 37, 59, 869061)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 19, 20, 37, 59, 869028)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='description',
            field=models.TextField(max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 20, 37, 59, 869521)),
            preserve_default=True,
        ),
    ]
