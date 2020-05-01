
from django.urls import path
from .views import CreateJobCallView,CompanyJobCallsView,JobCallDetailsView
urlpatterns = [
    path('create_jobcall', CreateJobCallView.as_view(), name='company.create_jobcall'),
    path('', CompanyJobCallsView.as_view(), name='company.jobcalls'),
    path('details/<int:pk>/', JobCallDetailsView.as_view(), name='article-detail'),
]
