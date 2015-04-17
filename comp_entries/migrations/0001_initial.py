# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('deadline_date', models.DateField(default=datetime.datetime(2015, 4, 2, 21, 19, 0, 902039))),
                ('creation_date', models.DateField(default=datetime.datetime(2015, 3, 3, 21, 19, 0, 902076))),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entrie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=50, blank=True)),
                ('entry_date', models.DateField(default=datetime.datetime(2015, 3, 3, 21, 19, 0, 902530))),
                ('entry_description', models.CharField(max_length=200, blank=True)),
                ('competition_name', models.ForeignKey(to='comp_entries.Competition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
