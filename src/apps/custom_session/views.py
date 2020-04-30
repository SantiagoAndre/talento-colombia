from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import  LoginView
from django.shortcuts import render
from django.conf import settings


User = get_user_model()
class LoginView(LoginView):
    #form_class=LoginForm
    form_class = AuthenticationForm
    redirect_authenticated_user=True
    template_name = 'registration/login.html'
    def get_success_url(self):
        
        if self.request.user.is_superuser:
            return settings.LOGIN_ADMIN_REDIRECT_URL
        if self.request.user.is_company:
            return settings.LOGIN_COMPANY_REDIRECT_URL
        if self.request.user.is_aspirant:
            return settings.LOGIN_ASPIRING_REDIRECT_URL

