from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from landing import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Main Landing Page
    path('app-mcp/', admin.site.urls),
    path('join/', user_views.register, name='join'),  # Register Page
    path('shows/', include('shows.url')),  # Shows Apps Urls
    path('users/', include('users.url')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Login Page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')  # Logout Page
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
