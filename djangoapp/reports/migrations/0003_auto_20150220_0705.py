# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_reporttemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='data',
            field=models.TextField(default='data here ...'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='template',
            field=models.ForeignKey(default=1, to='reports.ReportTemplate'),
            preserve_default=False,
        ),
    ]
