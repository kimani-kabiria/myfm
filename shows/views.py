from django.views import generic
from .models import Station, Show, Episode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


# Shows List View
class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'shows/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['all_shows'] = Show.objects.all()
        context_data['all_radio'] = Station.objects.all()
        return context_data


# Show Details View
class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Show
    template_name = 'shows/details.html'


# Radio List View
class RadioView(LoginRequiredMixin, generic.ListView):
    template_name = 'shows/radio.html'
    context_object_name = 'all_radio'

    def get_queryset(self):
        return Station.objects.all()


# Radio Station Detail View
class StationView(LoginRequiredMixin, generic.DetailView):
    model = Station
    template_name = 'shows/station.html'

    def get_queryset(self):
        return Station.objects.all()



