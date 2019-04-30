from django.views import generic
from .models import Station, Show, Episode


# Shows List View
class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'all_shows'

    def get_queryset(self):
        return Show.objects.all()


# Show Details View
class DetailView(generic.DetailView):
    model = Show
    template_name = 'shows/details.html'


# Radio List View
class RadioView(generic.ListView):
    template_name = 'shows/radio.html'
    context_object_name = 'all_radio'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Station.objects.all()


# Radio Station Detail View
class StationView(generic.DetailView):
    model = Station
    template_name = 'shows/station.html'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Station.objects.all()



