
from django.urls import path
from .views import apply_jobcall,discard_jobcall
urlpatterns = [
    path('apply_jobcall/<int:jobcall_id>/', apply_jobcall, name='jobcall.user_apply'),
    path('discard_jobcall/<int:jobcall_id>/', discard_jobcall, name='jobcall.user_apply'),
]
