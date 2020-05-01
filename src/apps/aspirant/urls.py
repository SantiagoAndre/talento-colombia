
from django.urls import path
from .views import apply_jobcall,discard_jobcall,AllJobCallsView
urlpatterns = [
    path('', AllJobCallsView.as_view(), name='aspirant.jobcalls'),
    path('apply_jobcall/<int:jobcall_id>/', apply_jobcall, name='jobcall.user_apply'),
    path('discard_jobcall/<int:jobcall_id>/', discard_jobcall, name='jobcall.user_apply'),
]
