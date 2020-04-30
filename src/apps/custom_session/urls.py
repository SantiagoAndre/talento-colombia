from django.contrib.auth import views as auth_views
from .views import LoginView
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view() , name='logout'),

     
]
