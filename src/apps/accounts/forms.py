from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()
class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1','password2', 'user_type')

    def clean(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ('user_type','password','last_login','date_joined',)
       # fields = ('username','first_name','last_name','email','is_active','is_superuser','groups')
        required_fields = ('username','first_name','last_name','email')
    
    def valide_required_field(self,field):
        # add custom validation here
        fields = "username"
        data = self.cleaned_data
        if not data[field]:
            # is empty
            raise forms.ValidationError("%s is required" % field)
        return data[field]
    def clean_username(self):
        return self.valide_required_field('username')
    def clean_first_name(self):
        return self.valide_required_field('first_name')
    def clean_last_name(self):
        return self.valide_required_field('last_name')
    def clean_email(self):
        return self.valide_required_field('email')
