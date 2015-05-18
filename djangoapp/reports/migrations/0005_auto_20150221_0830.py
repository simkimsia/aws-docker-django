# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20150220_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='datetime_email_sent',
            field=models.DateTimeField(null=True, verbose_name=b'date email sent', blank=True),
            preserve_default=True,
        ),
    ]
