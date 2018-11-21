from django.views import generic
from .models import Station, Show, Episode


class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'all_shows'

    def get_queryset(self):
        return Show.objects.all()


class DetailView(generic.DetailView):
    model = Show
    template_name = 'shows/details.html'


class RadioView(generic.ListView):
    template_name = 'shows/radio.html'
    context_object_name = 'all_radio'

    def get_queryset(self):
        return Station.objects.all()


class StationView(generic.DetailView):
    model = Station
    template_name = ''
