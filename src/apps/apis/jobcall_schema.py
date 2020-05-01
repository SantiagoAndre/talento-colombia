import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from graphene_django.forms.types import ErrorType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from apps.jobcall.models import JobCall as JobCallModel

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

  
  #@login_required
  def resolve_jobcall(self, info, *args, **kwargs):
    id = kwargs.get('id')
    if id is not None:
      return JobCallModel.objects.get(pk=id)
    return None
  #@login_required
  def resolve_jobcalls(self, info, *args, **kwargs):
    return JobCallModel.objects.filter(**kwargs)# only actual company user  

from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation
from apps.company.forms import CreateJobCallForm
from apps.accounts.models import CompanyUser as C
class JobCallMutation(DjangoModelFormMutation):
  class Meta:
    form_class = CreateJobCallForm
  @login_required
  @classmethod
  def mutate_and_get_payload(cls, root, info, **input):
    form = cls.get_form(root, info, **input)
    if form.is_valid():
      form.instance.company = C.objects.first()
      return cls.perform_mutate(form, info)
    else:
      errors = ErrorType.from_errors(form.errors)
      return cls(errors=errors)
class Mutation(ObjectType):
  jobcall = JobCallMutation.Field()
