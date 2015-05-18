# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('commodity', models.CharField(max_length=10)),
                ('date', models.DateTimeField(verbose_name=b'date traded')),
                ('trade_period', models.CharField(default=b'open', max_length=10)),
                ('quantity_cutoff', models.IntegerField(default=0)),
                ('printed', models.BooleanField(default=0)),
                ('datetime_email_sent', models.DateTimeField(verbose_name=b'date email sent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
