
from django.views.generic import CreateView,View,DetailView
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.shortcuts import render

from .forms import CreateJobCallForm
from apps.jobcall.models import JobCall
from apps.custom_session.decorators import role_required

User = get_user_model()
# Create your views here.
@method_decorator(role_required(rol=User.COMPANY),name="dispatch")
class CreateJobCallView(CreateView):
  
    form_class = CreateJobCallForm
    template_name = 'company/create_jobcall.html'
    success_url = '/company'
    def form_valid(self, form):
        #form.instance.jobcall = JobCall.objects.get(pk=self.kwargs['jobcall_id'])
        form.instance.company = self.request.user
        return super().form_valid(form)
  
@method_decorator(role_required(rol=User.COMPANY),name="dispatch")
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

@method_decorator(role_required(rol=User.COMPANY),name="dispatch")
class JobCallDetailsView(DetailView):
  model = JobCall
  template_name = 'company/jobcall_details.html'
  queryset = JobCall.objects.all()
