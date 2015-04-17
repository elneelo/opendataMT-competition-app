# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0002_auto_20150303_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 3, 21, 19, 49, 545565)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 2, 21, 19, 49, 545528)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrie',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 3, 21, 19, 49, 546060)),
            preserve_default=True,
        ),
    ]
