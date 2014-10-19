# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('flag', models.ImageField(upload_to=b'/uploads/images/countries')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('event_kml', models.FileField(upload_to=b'/kml', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDistance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.CharField(default=b'100M', max_length=4, choices=[(b'100M', b'100 Mile'), (b'50M', b'50 Mile'), (b'100K', b'100 Kilometers'), (b'50K', b'50 Kilometers')])),
                ('active', models.BooleanField()),
                ('event', models.ForeignKey(to='iRFmap.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('elevation', models.IntegerField()),
                ('latitude', models.DecimalField(max_digits=7, decimal_places=3)),
                ('longitude', models.DecimalField(max_digits=7, decimal_places=3)),
                ('photo', models.ImageField(upload_to=b'/uploads/images/locations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('location_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iRFmap.Location')),
                ('title', models.CharField(max_length=50)),
                ('mileage', models.FloatField()),
            ],
            options={
            },
            bases=('iRFmap.location',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(upload_to=b'uploads/images/runners', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('event', models.ForeignKey(related_name=b'runners', to='iRFmap.Event')),
                ('person', models.ForeignKey(to='iRFmap.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RunnerStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=255)),
                ('runner', models.ForeignKey(to='iRFmap.Runner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='race',
            field=models.ForeignKey(to='iRFmap.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='person',
            field=models.ForeignKey(to='iRFmap.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='event',
            field=models.ForeignKey(related_name=b'checkpoints', to='iRFmap.Event'),
            preserve_default=True,
        ),
    ]
