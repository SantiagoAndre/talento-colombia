from django.urls import path,include


urlpatterns = [

    path('accounts', include('apps.accounts.urls')),
    path('jobcalls/', include('apps.jobcall.urls')),
    path('/', include('apps.custom_session.urls')),

]

