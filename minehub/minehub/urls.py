# minehub/urls.py
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('', include('home.urls')),  # Route the root URL to home.urls
    path('', home_views.home, name='home'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

