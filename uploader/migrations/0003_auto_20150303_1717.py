# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20150227_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='pic',
            field=models.FileField(upload_to=b'uploaded_files/', verbose_name=b'Image'),
            preserve_default=True,
        ),
    ]
