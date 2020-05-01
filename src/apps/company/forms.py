from django.utils.timezone import datetime #important if using timezones
from django import forms
from apps.jobcall.models import JobCall


class CreateJobCallForm(forms.ModelForm):
    class Meta:
        model = JobCall
        fields = ('position','description','closing_date','state')
        widgets = {
            'closing_date': forms.DateInput(format='%Y-%m-%d',
            attrs={'class': 'form_datetime','type':'date','min':datetime.today().strftime("%Y-%m-%d")}),
           
        }
    def save(self, commit=True): 
        return super().save(commit=commit)

