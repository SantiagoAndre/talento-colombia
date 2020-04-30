
from django.views.generic import CreateView
from django.shortcuts import redirect,render
from django.views import View
from apps.accounts.models import AspiringUser
# Create your views here.
from .forms import ApplyJobCallForm
from .models import JobCall,AnonymousInscription



def all_jobcalls(request):
  context = {
    'jobcalls': JobCall.objects.all().order_by('-closing_date')
  }
  return render(request, 'jobcall/list_jobcalls.html', context=context)

def user_apply(request,jobcall_id=None):
  jobcall = JobCall.objects.get(pk=jobcall_id)
  if jobcall.is_open:
    user = AspiringUser.objects.get(pk=request.user.id)
    jobcall.aspirants.add(user)
  return redirect('/')
  
def user_discard(request,jobcall_id=None):
  jobcall = JobCall.objects.get(pk=jobcall_id)
  if jobcall.is_open:
    user = AspiringUser.objects.get(pk=request.user.id)
    jobcall.aspirants.remove(user)
  return redirect('/')
  



class AllJobCallsView(View):
  def get(self, request): 
    context = {
    'jobcalls': JobCall.objects.all().order_by('-closing_date'),
    'apply_function': self.apply
    }
    return render(request, 'jobcall/list_jobcalls.html', context=context)

  def post(self, request):
    pass

  def push(self, request):
    pass
  def apply(self,jobcall):
    print(jobcall)

class ApplyJobCallView(CreateView):
  model = AnonymousInscription
  form_class = ApplyJobCallForm
  template_name = 'jobcall/apply.html'
  success_url = '/'
  def form_valid(self, form):
    form.instance.jobcall = JobCall.objects.get(pk=self.kwargs['jobcall_id'])
    return super().form_valid(form)
  
#class 