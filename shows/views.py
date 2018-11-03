from django.http import HttpResponse
from django.shortcuts import render
from .models import Show


def index(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows,
    }
    return render(request, 'shows/index.html', context)


def detail(request, station_id):
    return HttpResponse("<h2>Details of Station id: " + str(station_id) + "</h2>")
