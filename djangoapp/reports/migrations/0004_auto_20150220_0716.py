# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20150220_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporttemplate',
            name='styles',
            field=models.TextField(default=b'styles here...'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='data',
            field=models.TextField(default=b'data here...'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reporttemplate',
            name='markup',
            field=models.TextField(default=b'markup here...'),
            preserve_default=True,
        ),
    ]
