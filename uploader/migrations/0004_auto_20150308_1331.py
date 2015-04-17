# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20150303_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='pic',
            field=models.FileField(upload_to=b'uploaded_files/', verbose_name=b'Submission File'),
            preserve_default=True,
        ),
    ]
