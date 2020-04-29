
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.conf.urls import url

from django.utils.html import format_html
from django.shortcuts import redirect
from django.urls import reverse

from admin_object_actions.admin import ModelAdminObjectActionsMixin


from .forms import *
from .models import *
# Register your models here.
User = get_user_model()



def details_function(*args):
    pass
@admin.register(User)
class SnippetAdmin(ModelAdminObjectActionsMixin,admin.ModelAdmin):
    add_form = UserCreationForm
    change_form = UserChangeForm
    list_display = ('username','email','first_name',
                     'last_name','user_type',
                    'display_object_actions_list')
    list_filter =  ('user_type',)

    readonly_fields = (
        'display_object_actions_detail',
    )   
    object_actions = [
        {
            'slug': 'details_action',
            'verbose_name': _('details'),
            'function': details_function,
            'readonly_fields': ['username','first_name','last_name','email','is_active','is_superuser','groups'],
            'permission': 'view',
            'list_only':True
        }
    ]
    
    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(SnippetAdmin, self).get_form(request, obj, **kwargs)
    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/accounts/accounts/user')

#admin.site.unregister(Group)
