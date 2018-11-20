from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Show, Station, Episode


def index(request):
    all_shows = Show.objects.all()
    context = {'all_shows': all_shows, }
    return render(request, 'shows/index.html', context)


def detail(request, show_id):
    try:
        show = Show.objects.get(pk=show_id)
    except Show.DoesNotExist:
        raise Http404("Show does not exist")
    return render(request, 'shows/details.html', {'show': show})


def featured_detail(request):
    all_shows = Show.objects.all()
    contexxt = {'all_shows': all_shows, }
    return render(request, 'shows/details.html', contexxt)


def stations(request):
    all_stations = Station.objects.all()
    ccontext = {'all_stations': all_stations}
    return render(request, 'shows/radio.html', ccontext)
