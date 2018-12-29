from django.views import generic
from django.views.generic import TemplateView
from .models import Station, Show, Episode


class IndexView(TemplateView):
    context_object_name = 'index_view'
    template_name = 'shows/index.html'
    queryset = Show.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_shows'] = Show.objects.all()
        context['all_radio'] = Station.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Show
    template_name = 'shows/single-show.html'
    slug_url_kwarg = 'slug'


class RadioView(generic.ListView):
    template_name = 'shows/radio.html'
    context_object_name = 'all_radio'

    def get_queryset(self):
        return Station.objects.all()


class StationView(generic.DetailView):
    model = Station
    template_name = 'shows/single-station.html'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'
