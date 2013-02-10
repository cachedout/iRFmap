from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from models import *

def map(request):
    if settings.DEBUG: print "DEBUG: views::map() Entered map()"
#    leaders = 
    return render(request, 'base.html')

def poll_for_all(request, item):
    if settings.DEBUG: print "DEBUG: views::poll_for() Entered poll_for()"

    items = models.item

    return None