from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def map(request):
    if settings.DEBUG: print "DEBUG: views::map() Entered map()"
    return render(request, 'map.html')