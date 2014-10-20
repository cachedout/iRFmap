# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iRFmap', '0003_auto_20141019_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runnerstatus',
            name='runner',
        ),
        migrations.AddField(
            model_name='event',
            name='preview_url',
            field=models.URLField(default=b'http://irunfar.com', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='distance',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='distance',
            field=models.CharField(default=b'100M', max_length=4),
        ),
    ]
