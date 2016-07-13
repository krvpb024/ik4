from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = [
        "username", 
        "password1", 
        "password2", 
        "email", 
        "last_name", 
        "first_name",
        ]
        labels = {
        "username":"帳號", 
        }
    	
    def save(self, commit=True):
    	user = super(UserCreateForm, self).save(commit=False)
    	user.email = self.cleaned_data["email"]
    	user.last_name = self.cleaned_data["last_name"]
    	user.first_name = self.cleaned_data["first_name"]
    	if commit:
    		user.save()
    	return user