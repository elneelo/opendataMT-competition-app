# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0025_auto_20150316_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 18, 31, 26, 478490)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 18, 31, 26, 478456)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 16, 18, 31, 26, 478944)),
            preserve_default=True,
        ),
    ]
