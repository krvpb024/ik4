from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, UserEditForm, PasswordChangeForm
from articles.models import Article, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
	

@login_required
def edit_profile(request, user_name):
	user = get_object_or_404(User, username=user_name)
	form = UserEditForm(instance=user)
	
	if user.username != request.user.username:
		messages.add_message(request, messages.INFO, '你並非此使用者，沒有權限修改')
		return HttpResponseRedirect('/profile_view/' + str(user.username))	

	if request.method == "POST":
		form = UserEditForm(instance=user, data=request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, '編輯完成')
			return HttpResponseRedirect('/profile_view/' + str(user.username))
	return render(request, 'edit_profile.html', {'form': form})
	



@login_required
def password_change(request, user_name):
	user = get_object_or_404(User, username=user_name)
	
	if user.username != request.user.username:
		messages.add_message(request, messages.INFO, '你並非此使用者，沒有權限修改')
		return HttpResponseRedirect('/profile_view/' + str(user.username))	
		
	if request.method == "POST":
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.add_message(request, messages.INFO, '密碼更改完成')
			return HttpResponseRedirect('/profile_view/' + str(user.username))
	else:
		form = PasswordChangeForm(user=request.user)	
	return render(request, 'password_change_form.html', {'form': form})