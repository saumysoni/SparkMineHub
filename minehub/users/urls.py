from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('logout/', views.logout, name='logout'),
    path('logout/', views.custom_logout, name='logout'),
]
