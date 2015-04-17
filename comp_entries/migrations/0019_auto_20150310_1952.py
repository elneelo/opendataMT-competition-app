# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0018_auto_20150310_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 10, 19, 52, 33, 335299)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 9, 19, 52, 33, 335264)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='description',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 10, 19, 52, 33, 335799)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='entry_description',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
