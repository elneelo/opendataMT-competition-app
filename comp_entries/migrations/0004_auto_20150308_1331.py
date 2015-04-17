# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0003_auto_20150303_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=50, blank=True)),
                ('entry_date', models.DateField(default=datetime.datetime(2015, 3, 8, 13, 31, 13, 117092))),
                ('entry_description', models.CharField(max_length=200, blank=True)),
                ('competition_name', models.ForeignKey(to='comp_entries.Competition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='entrie',
            name='competition_name',
        ),
        migrations.DeleteModel(
            name='Entrie',
        ),
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 13, 31, 13, 116638)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 7, 13, 31, 13, 116604)),
            preserve_default=True,
        ),
    ]
