from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('app-mcp/', admin.site.urls),
    path('join/', user_views.register, name='join'),
    path('shows/', include('shows.url')),
    path('users/', include('users.url'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
