from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from taggit.models import Tag
from django.contrib import messages
from django.db.models import Q

# Create your views here.
from . import forms
from .models import Article, Comment

def article_list(request):
	articles = Article.objects.all()
	query = request.GET.get('q')
	if query:
		articles = Article.objects.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(author__username__iexact=query)|
			Q(tags__name__icontains=query)
			).distinct()
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
def article_delete(request, pk):
	articles = get_object_or_404(Article, pk=pk)
	author = articles.author
	
	if author != request.user:
		messages.add_message(request, messages.INFO, '你並非發文者，無刪除此文章權限')
		return HttpResponseRedirect('/article/' + str(articles.pk))
	else:
		articles.delete()
		messages.add_message(request, messages.INFO, '文章已刪除')
		return HttpResponseRedirect('/article/')
	return render(request, 'article_detail.html', {'articles': articles})

@login_required
def comment_delete(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	articles = comment.article
	comment_author = comment.author
	
	if comment_author != request.user:
		messages.add_message(request, messages.INFO, '你並非回應者，無刪除此回應權限')
		return HttpResponseRedirect('/article/' + str(articles.pk))
	else:
		comment.delete()
		messages.add_message(request, messages.INFO, '回應已刪除')
		return HttpResponseRedirect('/article/' + str(articles.pk))
	return render(request, 'article_detail.html', {'articles': articles})
	
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
	
	
