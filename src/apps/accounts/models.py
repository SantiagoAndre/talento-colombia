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
class AspiringUser(User):
    # fields
    # career, etc
    pass


class CompanyUser(User):
    #fields 
    # type company, etc
    pass

