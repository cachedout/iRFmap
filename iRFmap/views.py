from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from models import *
import jsonpickle as json

def encode_to_json(obj):
#    return json.dumps(obj.values())
    return serializers.serialize("json", obj, ensure_ascii=False)


def map(request):
    if settings.DEBUG: print "DEBUG: views::map() Entered map()"
#    leaders = 
    return render(request, 'base.html')

def poll_leaderboard(request, race_id):
    leaderboard = {}
    leaderboard_queryset = Race.objects.get(id=race_id).leaderboard()
    for runner in leaderboard_queryset.all():
        leaderboard[runner.position] = runner.person
    leaderboard = json.encode(leaderboard, unpicklable=False)
    return HttpResponse(leaderboard, content_type='application/json')
   


