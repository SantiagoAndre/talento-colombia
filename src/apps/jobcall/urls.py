
from django.urls import path
from .views import all_jobcalls,AllJobCallsView
urlpatterns = [
    path('', AllJobCallsView.as_view(), name='jobcall.jobcalls'),
  #  path('apply/<int:jocall_id>/', all_jobcalls, name='jobcall.apply'),
]
