from django.http import HttpResponse
from django.template import loader
from .models import Show


def index(request):
    all_shows = Show.objects.all()
    html = ''
    for show in all_shows:
        url = '/shows/' + str(show.id) + '/'
        html += '<a href="' + url + '">' + show.shw_title + '</a><br>'
    return HttpResponse(html)


def detail(request, station_id):
    return HttpResponse("<h2>Details of Station id: " + str(station_id) + "</h2>")
