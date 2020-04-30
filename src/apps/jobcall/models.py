from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import CompanyUser, AspiringUser
# Create your models here.


class JobCall(models.Model):
    OPEN =1
    CLOSED= 2
    FINISHED = 3
    STATES = (
        (OPEN, 'open'),
        (CLOSED, 'close'),
        (FINISHED, 'finished'),
    )
    closing_date = models.DateTimeField(_("closing date"))
    position = models.CharField(_("position"),max_length=150)
    description = models.TextField(_("description"))
    state = models.PositiveSmallIntegerField(choices=STATES,default=OPEN,verbose_name = _("state"))
    company = models.ForeignKey(CompanyUser,verbose_name=_("company"),on_delete=models.CASCADE)
    aspirants = models.ManyToManyField(AspiringUser,verbose_name=_("aspirants"),blank=True)
    
    

    class Meta:
        order_with_respect_to = 'closing_date'
        verbose_name = _('job call')
        verbose_name_plural = _('job calls')

class AnonymousInscription(models.Model):
    full_name = models.CharField(_("full name"),max_length=150)
    jobcall = models.ForeignKey(JobCall,on_delete=models.CASCADE,verbose_name=_("anonymous aspirants"),blank=True)
    #file = pk.pdf
