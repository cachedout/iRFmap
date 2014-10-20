import datetime
from django.db import models


class Race(models.Model):
    ''' An event that re-occurs over time, presumeably a race that happens once a year. '''
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age = models.IntegerField()
    photo = models.ImageField(upload_to='uploads/images/runners', blank=True)

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)

class Distance(models.Model):
    distance = models.CharField(max_length=4, default='100M')
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.distance

class Event(models.Model):
    '''An instance of an Race. e.g., the race that is happening this year'''
    date = models.DateField(default=datetime.date.today)
    description = models.TextField()
    race = models.ForeignKey(Race)
    distance = models.ForeignKey(Distance)
    event_kml = models.FileField(upload_to='/kml', blank=True)
    preview_url = models.URLField(blank=True, default='http://irunfar.com')

    def __unicode__(self):
        return '{race} {distance} {date}'.format(race=self.race,
                                                 distance=self.distance,
                                                 date=self.date)

    def leaderboard(self):
        '''
        Orders the leaders and returns the entire set
        Args:
        Returns: 
            A list of Runners ordered by position
        '''
        return Event.objects.select_related().filter(race=self).order_by('position')

class RunnerStatus(models.Model):
    STATUS_OPTS =(
            ('PRE_START', 'Waiting for race start'),
            ('DNF', 'Did not finish'),
            ('DNS', 'Did not start'),
            ('ON_COURSE', 'On course'),
            ('FINISHED', 'Finished'),
            ('DNF_INJURY', 'Did not finish due to injury'),
            )
    status = models.CharField(max_length=255, choices=STATUS_OPTS, default='PRE_START')

    def __unicode__(self):
        return self.status

class Location(models.Model):
    elevation = models.IntegerField()  # FIXME handle feet vs. meters
    latitude = models.DecimalField(max_digits=7, decimal_places=3)
    longitude = models.DecimalField(max_digits=7, decimal_places=3)
    photo = models.ImageField(upload_to='/uploads/images/locations')

class Runner(models.Model):
    ''' Represents a runner actually in a particular event '''
    position = models.IntegerField()
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event, related_name='runners')
    status = models.ForeignKey(RunnerStatus)
    bib = models.IntegerField(blank=True, default=0)

    def __unicode__(self):
        return '{last_name}, {first_name} #{bib}'.format(last_name=self.person.last_name,
                                                         first_name=self.person.first_name,
                                                         bib=self.bib)

class Checkpoint(Location):
    title = models.CharField(max_length=50)
    mileage = models.FloatField()
    event = models.ForeignKey(Event, related_name='checkpoints')
    runners = models.ManyToManyField(Runner, through='RunnerPosition')

    def __unicode__(self):
        return self.title

class RunnerPosition(models.Model):
    '''
    The heart of the beast. Tracks runners as they progress
    through the course
    '''
    runner = models.ForeignKey(Runner)
    checkpoint = models.ForeignKey(Checkpoint)
    arrival = models.DateField(default=datetime.date.today)

class Country(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='/uploads/images/countries')
    person = models.ForeignKey(Person)
   
    def __unicode__(self):
       return self.name
