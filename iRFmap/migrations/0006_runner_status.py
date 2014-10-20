# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iRFmap', '0005_auto_20141019_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='status',
            field=models.ForeignKey(default=0, to='iRFmap.RunnerStatus'),
            preserve_default=False,
        ),
    ]
