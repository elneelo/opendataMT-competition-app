# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comp_entries', '0058_competition_teams'),
        ('uploader', '0004_auto_20150308_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='pic',
            new_name='submission',
        ),
        migrations.AddField(
            model_name='upload',
            name='competition',
            field=models.ForeignKey(default=1, to='comp_entries.Competition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='team',
            field=models.ForeignKey(default=1, to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.DateTimeField(verbose_name=b'upload date'),
            preserve_default=True,
        ),
    ]
