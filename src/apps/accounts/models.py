from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils.translation import gettext_lazy as _
#from apps.jobcall.models import JobCall

# Create your models here.

class User(AbstractUser):
    ASPIRING =1
    COMPANY = 2
    ADMIN = 3
    USER_TYPE_CHOICES = (
        (ASPIRING, _('aspiring')),
        (COMPANY, _('company')),
        (ADMIN, _('admin')),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=ASPIRING,verbose_name=_("rol"))
    email = models.EmailField(unique=True,null=True)
    def __eq__(self,other):
        return  self.username == other.username
    def __hash__(self):
        return super(User,self).__hash__()
    @property
    def is_aspirant(self):
        return self.is_superuser or self.user_type == self.ASPIRING
    @property
    def is_company(self):
        return self.is_superuser or self.user_type == self.COMPANY
