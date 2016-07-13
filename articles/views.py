from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
from . import forms
from .models import Article


def article_list(request):
	articles = Article.objects.all()
	return render(request, 'article_list.html', {'articles':articles})

def article_detail(request, pk):
	articles = get_object_or_404(Article, pk=pk)
	return render(request, 'article_detail.html', {'articles':articles})	
	
@login_required
def create(request):
	form = forms.ArticleForm()
	
	if request.method == 'POST':
		form = forms.ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save(commit=False)
			new_article.author = request.user
			new_article.save()
			return HttpResponseRedirect('/article/' + str(new_article.pk))
	return render(request, 'create.html', {'form': form})
	
"""
	def create_HashTag(request):
		form = forms.HashTagForm()
		if request.method == 'POST':
			form = forms.HashTagForm(request.POST)
			if form.is_valid():
				if form[0] == "#":
					new_hashtag = form.cleaned_data['name'].split(" ")
"""	
	
@login_required
def create_comment(request, pk):
	articles = get_object_or_404(Article, pk=pk)
	form = forms.CommentForm
	
	if request.method == 'POST':
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.article = articles
			comment.author = request.user
			comment.save()
			return HttpResponseRedirect('/article/' + str(pk))
	return render(request, 'create_comment.html', {'form': form, 'articles':articles})