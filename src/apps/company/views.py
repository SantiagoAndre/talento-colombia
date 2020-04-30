from apps.accounts.models import CompanyUser
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import CreateJobCallForm
# Create your views here.
class CreateJobCallView(CreateView):
  
    form_class = CreateJobCallForm
    template_name = 'company/create_jobcall.html'
    success_url = '/'
    def form_valid(self, form):
        #form.instance.jobcall = JobCall.objects.get(pk=self.kwargs['jobcall_id'])
        form.instance.company = CompanyUser.objects.get(pk=self.request.user.id)
        return super().form_valid(form)
  
#class 