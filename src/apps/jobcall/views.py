from django.shortcuts import render

from django.views import View
# Create your views here.
from .models import JobCall

def all_jobcalls(request):
  context = {
    'jobcalls': JobCall.objects.all().order_by('-closing_date')
  }
  return render(request, 'jobcall/list_jobcalls.html', context=context)


class AllJobCallsView(View):
  def get(self, request): 
    context = {
    'jobcalls': JobCall.objects.all().order_by('-closing_date')
    }
    return render(request, 'jobcall/list_jobcalls.html', context=context)

  def post(self, request):
    pass

  def push(self, request):
    pass

#class 