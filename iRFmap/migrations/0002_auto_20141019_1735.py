# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iRFmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.CharField(default=b'100M', max_length=4, choices=[(b'100M', b'100 Mile'), (b'50M', b'50 Mile'), (b'100K', b'100 Kilometers'), (b'50K', b'50 Kilometers')])),
                ('active', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='eventdistance',
            name='event',
        ),
        migrations.DeleteModel(
            name='EventDistance',
        ),
        migrations.AddField(
            model_name='event',
            name='distance',
            field=models.ForeignKey(default=1, to='iRFmap.Distance'),
            preserve_default=False,
        ),
    ]
