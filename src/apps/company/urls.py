
from django.urls import path
from .views import CreateJobCallView,CompanyJobCallsView
urlpatterns = [
    path('create_jobcall', CreateJobCallView.as_view(), name='company.create_jobcall'),
    path('', CompanyJobCallsView.as_view(), name='company.jobcalls'),
]
