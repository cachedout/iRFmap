# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iRFmap', '0007_auto_20141019_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='runner',
            name='bib',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
