from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .models import JobCall,AnonymousInscription


def apply_jobcall(sender, instance, **kwargs):
	if not  instance.is_open:
		raise Exception(_("jobcall is closed"))

#presave in  inscription manytomany field
@receiver(pre_save, sender=AnonymousInscription) 
def anonymouns_appy_jobcall(sender, instance, **kwargs):
	if not  instance.jobcall.is_open:
		raise Exception(_("jobcall is closed"))


m2m_changed.connect(apply_jobcall, sender=JobCall.aspirants.through)

