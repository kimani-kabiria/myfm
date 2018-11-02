from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>This is the Shows APP Homepage</H1>")
