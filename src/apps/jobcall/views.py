
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



class AllJobCallsView(View):
  def get(self, request): 
    context = {
    'jobcalls': JobCall.objects.all().order_by('closing_date'),
    }
    return render(request, 'jobcall/list_jobcalls.html', context=context)

  def post(self, request):
    pass

  def push(self, request):
    pass

class ApplyJobCallView(CreateView):
  model = AnonymousInscription
  form_class = ApplyJobCallForm
  template_name = 'jobcall/apply.html'
  success_url = '/'
  def form_valid(self, form):
    form.instance.jobcall = JobCall.objects.get(pk=self.kwargs['jobcall_id'])
    return super().form_valid(form)
  
#class 