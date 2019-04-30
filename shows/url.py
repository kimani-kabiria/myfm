from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    # Main Shows app URLS

    # Shows Index
    path('', views.IndexView.as_view(), name='index'),

    # Individual Station Url
    path('<slug>/', views.DetailView.as_view(), name='show'),

    # Radio List Url
    path('radio', views.RadioView.as_view(), name='radio'),

    # Individual Radio Url
    path('radio/<slug>/', views.StationView.as_view(), name='stations'),

]
