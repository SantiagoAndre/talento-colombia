from django.shortcuts import redirect
from apps.jobcall.models import JobCall
from apps.accounts.models import AspiringUser

# Create your views here.

def apply_jobcall(request,jobcall_id=None):
  jobcall = JobCall.objects.get(pk=jobcall_id)
  if jobcall.is_open:
    user = AspiringUser.objects.get(pk=request.user.id)
    jobcall.aspirants.add(user)
  return redirect('/')
  
def discard_jobcall(request,jobcall_id=None):
  jobcall = JobCall.objects.get(pk=jobcall_id)
  if jobcall.is_open:
    user = AspiringUser.objects.get(pk=request.user.id)
    jobcall.aspirants.remove(user)
  return redirect('/')
  