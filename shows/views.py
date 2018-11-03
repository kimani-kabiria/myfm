from django.http import HttpResponse
from django.template import loader
from .models import Show


def index(request):
    all_shows = Show.objects.all()
    template = loader.get_template('shows/index.html')
    context = {
        'all_shows': all_shows,
    }
    return HttpResponse(template.render(context, request))


def detail(request, station_id):
    return HttpResponse("<h2>Details of Station id: " + str(station_id) + "</h2>")
