from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm

def index(request):
    return render_to_response('index.html',locals())
    
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/article/')
    
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/?next=/article/')
    else:
        form = UserCreateForm()
    return render(request, 'register.html',locals())