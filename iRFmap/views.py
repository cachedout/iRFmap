import logging

from django.shortcuts import render
from django.http import HttpResponse

from models import *
import jsonpickle as json


def map_view(request):
    """

    :param request: Incoming request
    :return: rendered response
    """
    logging.log(1, 'Entered map_view()')
    return render(request, 'map.html')


def poll_leaderboard(request, race_id):
    leaderboard = Runner.objects.select_related().filter(race__id=race_id).order_by('position')
    context = [leader.person for leader in leaderboard]
    return HttpResponse(json.encode(context, unpicklable=False), content_type='application/json')
   


