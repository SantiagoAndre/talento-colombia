
from django.urls import path
from .views import CreateJobCallView
urlpatterns = [
    path('create_jobcall', CreateJobCallView.as_view(), name='company.create_jobcall'),
]
