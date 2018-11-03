from django.urls import path
from . import views

urlpatterns = [
    # Shows Index
    path('', views.index, name='Index'),

    # Individual Station Url
    path('<int:station_id>/', views.detail, name='Detail'),
]
