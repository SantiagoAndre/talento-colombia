from apps.accounts.models import CompanyUser
from django.views.generic import CreateView,View,DetailView
from django.shortcuts import render
from .forms import CreateJobCallForm
from apps.jobcall.models import JobCall
# Create your views here.
class CreateJobCallView(CreateView):
  
    form_class = CreateJobCallForm
    template_name = 'company/create_jobcall.html'
    success_url = '/company'
    def form_valid(self, form):
        #form.instance.jobcall = JobCall.objects.get(pk=self.kwargs['jobcall_id'])
        form.instance.company = CompanyUser.objects.get(pk=self.request.user.id)
        return super().form_valid(form)
  
class CompanyJobCallsView(View):
  def get(self, request): 
    context = {
    'jobcalls': JobCall.objects.filter(company__id=request.user.id).order_by('closing_date'),
    }
    return render(request, 'jobcall/list_jobcalls.html', context=context)

  def post(self, request):
    pass

  def push(self, request):
    pass
  def apply(self,jobcall):
    print(jobcall)

class JobCallDetailsView(DetailView):
  model = JobCall
  template_name = 'company/jobcall_details.html'
  queryset = JobCall.objects.all()
