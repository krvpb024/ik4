from django import forms

from . import models

class ArticleForm(forms.ModelForm):

	class Meta:
		model = models.Article
		fields = [
		'title',
		'content',
		'tags',
		]
		labels = {
        "title": "標題",
        "content":"內容",
        "tags":"標籤",
    	}
		help_texts = {
    	'tags':'使用逗號區隔'
    	}
    	
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = [
		'content',
		]
		labels = {
        "content":"回應內容",
    	}
    	
    	