from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    # Main app URLS
    # Shows Index
    path('', views.IndexView.as_view(), name='index'),

    path('register', views.UserRegFormView.as_view(), name='register'),

    # Individual Station Url
    path('<slug>/', views.DetailView.as_view(), name='show'),

    path('radio', views.RadioView.as_view(), name='radio'),

    path('radio/<slug>/', views.StationView.as_view(), name='stations'),

]
