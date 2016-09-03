from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from taggit.models import Tag
from django.contrib import messages

# Create your views here.
from . import forms
from .models import Article

def article_list(request):
	articles = Article.objects.all()
	return render(request, 'article_list.html', {'articles':articles})


def article_detail(request, pk):
	articles = get_object_or_404(Article, pk=pk)
	return render(request, 'article_detail.html', {'articles':articles})
		
		
def tagged(request, slug):
	tags = get_object_or_404(Tag, slug=slug)
	articles = Article.objects.filter(tags__slug=slug)
	context = {'tags': tags, 'articles': articles}
	return render(request, 'article_list.html', context)
    
	
@login_required
def create(request):
	form = forms.ArticleForm()
	
	if request.method == 'POST':
		form = forms.ArticleForm(request.POST)
		if form.is_valid():
			new_article = form.save(commit=False)
			new_article.author = request.user
			new_article = form.save()
			messages.add_message(request, messages.INFO, '文章發表完成')
			return HttpResponseRedirect('/article/' + str(new_article.pk))
	return render(request, 'create.html', {'form': form})


@login_required
def article_edit(request, article_pk):
	article = get_object_or_404(Article, pk=article_pk)
	author = article.author
	form = forms.ArticleForm(instance=article)
	
	if author != request.user:
		messages.add_message(request, messages.INFO, '你並非發文者，無編輯此文章權限')
		return HttpResponseRedirect('/article/' + str(article.pk))
	
	if request.method =='POST':
		form = forms.ArticleForm(instance=article, data=request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, '編輯完成')
			return HttpResponseRedirect('/article/' + str(article.pk))
	return render(request, 'create.html', {'form': form})

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
			messages.add_message(request, messages.INFO, '回應發表完成')
			return HttpResponseRedirect('/article/' + str(pk))
	return render(request, 'create_comment.html', {'form': form, 'articles':articles})
	
	
