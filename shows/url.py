from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    # Main Shows app URLS

    # Shows Index
    path('', views.IndexView.as_view(), name='index'),

    # Individual Show Url
    path('<slug>/', views.DetailView.as_view(), name='show'),

    # Radio List Url
    path('all-radio', views.RadioView.as_view(), name='station'),

    # Individual Radio Url
    path('station/<slug>/', views.StationView.as_view(), name='stations')

]
