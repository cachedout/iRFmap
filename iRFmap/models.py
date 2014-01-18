from django.db import models


class Event(models.Model):
    ''' An event that re-occurs over time, presumeably a race that happens once a year. '''
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    race_kml = models.FileField(upload_to='/kml', blank=True) #TESTME:Can we guarantee uniqueness?

    def __unicode__(self):
        return self.title


class EventDistance(models.Model):
    EVENT_DISTANCE = (
        ('100M', '100 Mile'),
        ('50M', '50 Mile'),
        ('100K', '100 Kilometers'),
        ('50K', '50 Kilometers')
    )

    distance = models.CharField(max_length=4, choices=EVENT_DISTANCE, default='100M')
    active = models.BooleanField()
    event = models.ForeignKey(Event)


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


class Race(models.Model):
    '''An instance of an Event. i.e., the race that is happening this year'''
    year = models.IntegerField()
    description = models.TextField()
    event = models.ForeignKey(Event)

    def leaderboard(self):
        '''
        Orders the leaders and returns the entire set
        Args:
        Returns: 
            A list of Runners ordered by position
        '''
        return Race.objects.select_related().filter(race=self).order_by('position')


class Runner(models.Model):
    ''' Represents a runner actually in a particular Race '''
    position = models.IntegerField()
    person = models.ForeignKey(Person)
    race = models.ForeignKey(Race, related_name='runners')


class RunnerStatus(models.Model):
    status = models.CharField(max_length=255)
    runner = models.ForeignKey(Runner)


class Location(models.Model):
    elevation = models.IntegerField()  # FIXME handle feet vs. meters
    latitude = models.DecimalField(max_digits=7, decimal_places=3)
    longitude = models.DecimalField(max_digits=7, decimal_places=3)
    photo = models.ImageField(upload_to='/uploads/images/locations')


# To think about:
# 1) What if the same checkpoint is the start and the finish?
class Checkpoint(Location):
    title = models.CharField(max_length=50)
    mileage = models.FloatField()
    #Will have to talk to Bryon about whether to FK this to race or to event
    race = models.ForeignKey(Event, related_name='checkpoints')


class Country(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='/uploads/images/countries')
    person = models.ForeignKey(Person)
    