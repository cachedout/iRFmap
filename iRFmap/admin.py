from models import *
from django.contrib import admin
from django import forms

    
class CheckpointInline(admin.TabularInline):
    model = Checkpoint
    #FIXME Ordering is dumb. See: http://paltman.com/2008/07/10/ordering-edit-inlines/
    
class EventDistanceForm(forms.ModelForm):
    class Meta:
        model=EventDistance
    
class EventAdmin(admin.ModelAdmin):
    form = EventDistanceForm
    
class EventInline(admin.TabularInline):
    model=Event
    form = EventDistanceForm
    list_display=('year', 'description', 'form')
    
class RunnerAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name')
    
class RaceAdmin(admin.ModelAdmin):
    list_display=('title', 'location')
    inlines = [EventInline]
    
    
admin.site.register(Race, RaceAdmin )
admin.site.register(Runner, RunnerAdmin)
admin.site.register(Event, EventAdmin)