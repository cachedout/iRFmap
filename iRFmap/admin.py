from models import *
from django.contrib import admin


class RunnerAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name')
    
admin.site.register(Race )
admin.site.register(Event)
admin.site.register(Runner, RunnerAdmin)
admin.site.register(Location)
admin.site.register(Checkpoint)