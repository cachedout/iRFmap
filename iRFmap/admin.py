from django.contrib import admin
from django import forms

from models import *


#class CheckpointInline(admin.TabularInline):
#    model = Checkpoint
    #FIXME Ordering is dumb. See: http://paltman.com/2008/07/10/ordering-edit-inlines/

class RunnerPositionInline(admin.TabularInline):
    model = RunnerPosition
    extra = 1

class RunnerInline(admin.TabularInline):
    model = Runner
    inlines = (RunnerPositionInline,)

class CheckpointInline(admin.TabularInline):
    model = Checkpoint
    inlines = (RunnerPositionInline,)

class EventAdmin(admin.ModelAdmin):
    '''
    Tracks events. Events are year+distance per race with a set of runners
    '''
    model = Event
    fields = ('date', 'race', 'description', 'distance', 'event_kml') 
    inlines = [RunnerInline, CheckpointInline]

class RaceAdmin(admin.ModelAdmin):
    '''
    Tracks races. Races are repeating events.
    '''
    model = Race

class PeopleAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('last_name', 'first_name')


class Admin(admin.ModelAdmin):
    list_display = ('title', 'location')


class DistanceAdmin(admin.ModelAdmin):
    model = Distance

class StatusAdmin(admin.ModelAdmin):
    model = RunnerStatus

admin.site.register(Event, EventAdmin)
admin.site.register(Distance, DistanceAdmin)
#admin.site.register(Runner, RunnerAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Person, PeopleAdmin)
admin.site.register(RunnerStatus, StatusAdmin)
