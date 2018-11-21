from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    # Shows Index
    path('', views.IndexView.as_view(), name='index'),

    # Individual Station Url
    path('<pk>/', views.DetailView.as_view(), name='show'),

    path('radio', views.RadioView.as_view(), name='radio'),

    path('radio/<pk>/', views.StationView.as_view(), name='stations'),

]
