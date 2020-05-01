from django.shortcuts import redirect,render
from apps.accounts.models import AspiringUser
from django.views import View

from apps.jobcall.models import JobCall




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

class AllJobCallsView(View):
  def get(self, request): 
    context = {
    'jobcalls': JobCall.objects.filter(aspirants__id=request.user.id).order_by('closing_date'),
    }
    return render(request, 'jobcall/list_jobcalls.html', context=context)

  def post(self, request):
    pass

  def push(self, request):
    pass