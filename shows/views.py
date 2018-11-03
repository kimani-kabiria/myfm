from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>This is the Shows APP Homepage</H1>")


def detail(request, station_id):
    return HttpResponse("<h2>Details of Station id: " + str(station_id) + "</h2>")
