from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from articles.models import Article, Comment
from django.contrib.auth.models import User

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
    
    
def user_profile(request, author_id):
	user = get_object_or_404(User, username=author_id)
	articles = Article.objects.filter(author=user)
	comments = Comment.objects.filter(author=user)
	context = {'articles':articles, 'comments':comments}
	return render(request, 'user_profile.html', context)
	