from django.contrib import admin
from django import forms

from models import *


class CheckpointInline(admin.TabularInline):
    model = Checkpoint
    #FIXME Ordering is dumb. See: http://paltman.com/2008/07/10/ordering-edit-inlines/


class EventDistanceForm(forms.ModelForm):
    EVENT_DISTANCE = (
        ('100M', '100 Mile'),
        ('50M', '50 Mile'),
        ('100K', '100 Kilometers'),
        ('50K', '50 Kilometers')
    )
    distance = forms.ChoiceField(choices=EVENT_DISTANCE)
    class Meta:
        model = Distance
        fields = ('distance',)


class RunnerInline(admin.TabularInline):
    model = Runner


class EventAdmin(admin.ModelAdmin):
    '''
    Tracks events. Events are year+distance per race with a set of runners
    '''
    model = Event
    form = EventDistanceForm
    fields = ('date', 'race', 'description', 'distance', 'event_kml') 
    inlines = [RunnerInline]

class RaceAdmin(admin.ModelAdmin):
    '''
    Tracks races. Races are repeating events.
    '''
    model = Race

#class EventInline(admin.TabularInline):
#    form = RaceDistanceForm
#    list_display = ('year', 'description', 'form')


class PeopleAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('last_name', 'first_name')


#class RunnerAdmin(admin.ModelAdmin):
#    list_display=('person')

class Admin(admin.ModelAdmin):
    list_display = ('title', 'location')
#    inlines = [RaceInline]

class Checkpoint(admin.ModelAdmin):
    model = Checkpoint


admin.site.register(Event, EventAdmin)
#admin.site.register(Runner, RunnerAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Person, PeopleAdmin)
