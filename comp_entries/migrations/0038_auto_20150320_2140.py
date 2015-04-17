# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0037_auto_20150320_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 21, 40, 44, 53682)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 19, 21, 40, 44, 53649)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 21, 40, 44, 54141)),
            preserve_default=True,
        ),
    ]
