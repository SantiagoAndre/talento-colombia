from django.contrib.auth import views as auth_views
from .views import LoginView
from django.urls import path,include
from django.conf import settings
urlpatterns = [
    path('/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
]
