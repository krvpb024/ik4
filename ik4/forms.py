from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangeForm(forms.Form):
	old_password = forms.CharField(required=True, widget=forms.PasswordInput())
	new_password1 = forms.CharField(required=True, widget=forms.PasswordInput())	
	new_password2 = forms.CharField(required=True, widget=forms.PasswordInput())
	
	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(PasswordChangeForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].error_messages = {'required': '你必須輸入舊密碼'}
		self.fields['new_password1'].error_messages = {'required': '你必須輸入新密碼'}
		self.fields['new_password2'].error_messages = {'required': '你必須再次輸入新密碼'}		
        
	def clean_old_password(self):
		old_password = self.cleaned_data['old_password']
		if not self.user.check_password(old_password):
			raise forms.ValidationError('舊密碼輸入錯誤')
		return old_password
	
	def clean_new_password2(self):
		password1 = self.cleaned_data.get('new_password1')
		password2 = self.cleaned_data.get('new_password2')
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError('兩次輸入密碼不同')
		return password2
		
	def save(self, commit=True):
		password = self.cleaned_data["new_password1"]
		self.user.set_password(password)
		if commit:
			self.user.save()
		return self.user
	
	

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=10)
    
    def __init__(self, *args, **kwargs):
    	super(UserCreateForm, self).__init__(*args, **kwargs)
    	self.fields['username'].error_messages = {'required': '你必須輸入帳號'}
    	self.fields['password1'].error_messages = {'required': '你必須輸入密碼'}
    	self.fields['password2'].error_messages = {'required': '你必須再次輸入密碼'}
    	self.fields['email'].error_messages = {'required': '你必須輸入信箱'}
    	self.fields['last_name'].error_messages = {'required': '你必須輸入您的性'}
    	self.fields['first_name'].error_messages = {'required': '你必須輸入您的名'}
        
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
        
    def clean_username(self):
    	username = self.cleaned_data['username']
    	try:
    		User.objects.get(username=username)
    	except User.DoesNotExist:
    		return username
    	raise forms.ValidationError('這個用戶名已經被註冊了，請使用另一個')        
    	
    def clean_password2(self):
    	password1 = self.cleaned_data['password1']
    	password2 = self.cleaned_data['password2']
    	
    	if password1 != password2:
    		raise forms.ValidationError("兩次輸入密碼不同")
    	return password2

        
    def clean_email(self):
    	email = self.cleaned_data['email']
    	try:
    		User.objects.get(email=email)
    	except User.DoesNotExist:
    		return email
    	raise forms.ValidationError('這個信箱已經被註冊了，請使用另一個')

        
    def save(self, commit=True):
    	user = super(UserCreateForm, self).save(commit=False)
    	user.email = self.cleaned_data["email"]
    	user.last_name = self.cleaned_data["last_name"]
    	user.first_name = self.cleaned_data["first_name"]
    	if commit:
    		user.save()
    	return user
    	

class UserEditForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    	super(UserEditForm, self).__init__(*args, **kwargs)
    	self.fields['email'].error_messages = {'required': '你必須輸入信箱'}
    	self.fields['last_name'].error_messages = {'required': '你必須輸入您的性'}
    	self.fields['first_name'].error_messages = {'required': '你必須輸入您的名'}


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    def clean_email(self):
    	email = self.cleaned_data['email']
    	current_user_email = self.instance.email
    	
    	if User.objects.filter(email__iexact=email).exclude(email__iexact=current_user_email):
    		raise forms.ValidationError('這個信箱已經被使用了，請使用另一個')
    	return email
    	
    def save(self, commit=True):
    	user = super(UserEditForm, self).save(commit=False)
    	user.email = self.cleaned_data["email"]
    	user.last_name = self.cleaned_data["last_name"]
    	user.first_name = self.cleaned_data["first_name"]
    	if commit:
    		user.save()
    	return user
    	
    	