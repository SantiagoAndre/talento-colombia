import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required,user_passes_test

from apps.jobcall.models import JobCall as JobCallModel

from .utils import is_company_user

class JobCall(DjangoObjectType):
  class Meta:
    model = JobCallModel
    filter_fields = {
      'position': ['exact', 'icontains', 'istartswith'],
      'description': ['icontains'],
      'state': ['exact'],
      'closing_date': ['gt', 'gte', 'lt', 'lte']
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  jobcalls = DjangoFilterConnectionField(JobCall)
  jobcall = graphene.Field(JobCall,
                                id=graphene.Int())

  @login_required
  @user_passes_test(is_company_user)
  def resolve_jobcall(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      user_id = info.context.user.id
      return JobCallModel.objects.filter(company__id=user_id).get(pk=id)
    return None
  
  @login_required
  @user_passes_test(is_company_user)
  def resolve_jobcalls(self, info, *args, **kwargs):
    user_id = info.context.user.id
    return JobCallModel.objects.filter(company__id=user_id,**kwargs)# only actual company user  

from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from apps.company.forms import CreateJobCallForm

class JobCallMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreateJobCallForm
  
  @classmethod
  @login_required
  @user_passes_test(is_company_user)
  def mutate_and_get_payload(cls, root, info, **input):
    print(input['closing_date'])
    form = cls.get_form(root, info, **input)
    if form.is_valid():
      company_user = info.context.user
      form.instance.company = company_user
      return cls.perform_mutate(form, info)
    else:
      errors = ErrorType.from_errors(form.errors)
      return cls(errors=errors)
class Mutation(ObjectType):
  jobcall = JobCallMutation.Field()
