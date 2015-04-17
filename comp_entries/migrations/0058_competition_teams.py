# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('comp_entries', '0057_auto_20150405_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='teams',
            field=models.ManyToManyField(to='teams.Team'),
            preserve_default=True,
        ),
    ]
