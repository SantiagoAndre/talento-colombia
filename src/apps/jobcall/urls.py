
from django.urls import path
from .views import ApplyJobCallView,AllJobCallsView
urlpatterns = [
    path('', AllJobCallsView.as_view(), name='jobcall.jobcalls'),
    path('apply/<int:jobcall_id>/', ApplyJobCallView.as_view(), name='jobcall.apply'),
]
