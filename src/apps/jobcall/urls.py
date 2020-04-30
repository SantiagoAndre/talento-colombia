
from django.urls import path
from .views import ApplyJobCallView,AllJobCallsView,user_apply,user_discard
urlpatterns = [
    path('', AllJobCallsView.as_view(), name='jobcall.jobcalls'),
    path('apply/<int:jobcall_id>/', ApplyJobCallView.as_view(), name='jobcall.apply'),
    path('user_apply/<int:jobcall_id>/', user_apply, name='jobcall.user_apply'),
    path('user_discard/<int:jobcall_id>/', user_discard, name='jobcall.user_apply'),
]
