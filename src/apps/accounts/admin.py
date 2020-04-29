from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .forms import *
from .models import *
# Register your models here.
User = get_user_model()

@admin.register(User)
class SnippetAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    change_form = UserChangeForm
    list_display = ('username','email','first_name','last_name','user_type')
    list_filter =  ('user_type',)
    

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(SnippetAdmin, self).get_form(request, obj, **kwargs)

admin.site.unregister(Group)
