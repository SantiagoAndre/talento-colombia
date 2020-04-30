
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import AnonymousInscription

class ApplyJobCallForm(forms.ModelForm):
    class Meta:
        model = AnonymousInscription
        fields = '__all__'
        widgets = {
            'curriculum': forms.FileInput(attrs={'class': 'form-control-file'})
        }
    def save(self, commit=True): 
        return super().save(commit=commit)