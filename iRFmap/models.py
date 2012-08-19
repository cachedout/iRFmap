from django.db import models

class Race (models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    race_kml = models.FileField(upload_to='/kml') #TESTME:Can we guarantee uniqueness?
    

class Event (models.Model):
    EVENT_DISTANCE = (
                      ('100M', '100 Mile'),
                      ('50M', '50 Mile'),
                      ('100K', '100 Kilometers'),
                      ('50K', '50 Kilometers'),
                    )
    
    year = models.IntegerField()
    description = models.TextField()
    race = models.ForeignKey(Race)
    distance = models.CharField(max_length=4, choices=EVENT_DISTANCE, default='100M')
    event_kml = models.FileField(upload_to='/kml')



    
class Runner (models.Model):
    
    GENDER_CHOICES = (
                      ('M', 'Male'),
                      ('F', 'Female'),
                      )
    
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    gender = models.CharField(max_length = 1, choices=GENDER_CHOICES, default='M')
    age = models.IntegerField()
    
class Location (models.Model):
    elevation = models.IntegerField() #FIXME handle feet vs. meters
    latitude = models.DecimalField(max_digits=7, decimal_places=3)
    longitude = models.DecimalField(max_digits=7, decimal_places=3)
    photo = models.ImageField(upload_to='/uploads/images/locations')
    
    
# To think about:
# 1) What if the same checkpoint is the start and the finish?
class Checkpoint (Location):
    title = models.CharField(max_length=50)
    mileage = models.FloatField()
    race = models.ForeignKey(Race)