from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Main app URLS
    # Shows Index
    path('', views.register, name='register'),

]
