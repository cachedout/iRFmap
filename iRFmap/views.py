from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import *

def map(request):
    if settings.DEBUG: print "DEBUG: views::map() Entered map()"
#    leaders = 
    return render(request, 'base.html')

def poll_leaderboard(request, race_id):
    if settings.DEBUG: print "DEBUG: views::poll_for() Entered poll_for()"
    race = Race.objects.get(id=race_id)
    print race

    leaderboard = race.leaderboard()
    leaderboard_json = serializers.serialize("python", leaderboard, ensure_ascii=False)
    if settings.DEBUG: print "DEBUG: views.poll_for() Returning JSON string, %s" % leaderboard_json
   
    return leaderboard_json