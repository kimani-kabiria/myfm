from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader, RequestContext


def home_view(request):
    context = {'home': 'landing'}
    return render_to_response('landing/home.html', context)

