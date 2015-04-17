# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0030_auto_20150317_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 18, 12, 24, 25, 416879)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 17, 12, 24, 25, 416844)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='description',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 18, 12, 24, 25, 417335)),
            preserve_default=True,
        ),
    ]
