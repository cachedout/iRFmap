# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iRFmap', '0006_runner_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunnerPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival', models.DateField(default=datetime.date.today)),
                ('checkpoint', models.ForeignKey(to='iRFmap.Checkpoint')),
                ('runner', models.ForeignKey(to='iRFmap.Runner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='runners',
            field=models.ManyToManyField(to='iRFmap.Runner', through='iRFmap.RunnerPosition'),
            preserve_default=True,
        ),
    ]
