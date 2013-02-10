from models import *
from django.contrib import admin
from django import forms

    
class CheckpointInline(admin.TabularInline):
    model = Checkpoint
    #FIXME Ordering is dumb. See: http://paltman.com/2008/07/10/ordering-edit-inlines/
    
class EventDistanceForm(forms.ModelForm):
    class Meta:
        model=EventDistance

class RunnerInline(admin.TabularInline):
    model=Runner
    
class RaceAdmin(admin.ModelAdmin):
    form = EventDistanceForm
    list_display=('year', 'event')
    inlines = [RunnerInline]
    
class RaceInline(admin.TabularInline):
    model=Race
    form = EventDistanceForm
    list_display=('year', 'description', 'form')

class PeopleAdmin(admin.ModelAdmin):
    model=Person
    list_display=('last_name', 'first_name')


    
#class RunnerAdmin(admin.ModelAdmin):
#    list_display=('person')
    
class EventAdmin(admin.ModelAdmin):
    list_display=('title', 'location')
    inlines = [RaceInline]
    
    
admin.site.register(Race, RaceAdmin )
#admin.site.register(Runner, RunnerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Person, PeopleAdmin)