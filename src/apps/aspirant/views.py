from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.shortcuts import redirect,render
from django.views import View


from apps.jobcall.models import JobCall
from apps.custom_session.decorators import role_required

User = get_user_model()

# Create your views here.
@role_required(rol=User.ASPIRING)
def apply_jobcall(request,jobcall_id=None):
  jobcall = JobCall.objects.get(pk=jobcall_id)
  jobcall.aspirants.add(request.user)
  return redirect('/')

@role_required(rol=User.ASPIRING)
def discard_jobcall(request,jobcall_id=None):
  jobcall = JobCall.objects.get(pk=jobcall_id)
  jobcall.aspirants.remove(request.user)
  return redirect('/')

@method_decorator(role_required(rol=User.ASPIRING),name="dispatch")
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