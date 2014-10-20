# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iRFmap', '0004_auto_20141019_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runnerstatus',
            name='status',
            field=models.CharField(default=b'PRE_START', max_length=255, choices=[(b'PRE_START', b'Waiting for race start'), (b'DNF', b'Did not finish'), (b'DNS', b'Did not start'), (b'ON_COURSE', b'On course'), (b'FINISHED', b'Finished'), (b'DNF_INJURY', b'Did not finish due to injury')]),
        ),
    ]
