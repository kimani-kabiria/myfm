from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app-mcp/', admin.site.urls),
    path('shows/', include('shows.url'))
]
