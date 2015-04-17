# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp_entries', '0056_auto_20150324_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='competition_name',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.AlterField(
            model_name='competition',
            name='creation_date',
            field=models.DateField(verbose_name=b'creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='competition',
            name='deadline_date',
            field=models.DateField(verbose_name=b'deadline date'),
            preserve_default=True,
        ),
    ]
