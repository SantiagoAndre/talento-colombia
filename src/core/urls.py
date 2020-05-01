from django.urls import path,include


urlpatterns = [

    path('accounts', include('apps.accounts.urls')),
    path('', include('apps.jobcall.urls')),
    path('sessions/', include('apps.custom_session.urls')),
    path('company/', include('apps.company.urls')),
    path('aspirant/', include('apps.aspirant.urls')),

]

