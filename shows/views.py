from django.views import generic
from .models import Station, Show, Episode
from django.contrib.auth.mixins import LoginRequiredMixin


# Shows List View
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'all_shows'
    context_object_name_2 = 'all_radio'

    def get_queryset(self):
        return Show.objects.all()


# Show Details View
class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Show
    template_name = 'shows/details.html'


# Radio List View
class RadioView(LoginRequiredMixin, generic.ListView):
    template_name = 'shows/radio.html'
    context_object_name = 'all_radio'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Station.objects.all()


# Radio Station Detail View
class StationView(LoginRequiredMixin, generic.DetailView):
    model = Station
    template_name = 'shows/station.html'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Station.objects.all()



