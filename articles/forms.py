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
    	
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = [
		'content',
		]
		labels = {
        "content":"回應內容",
    	}
    	
class HashTagForm(forms.ModelForm):
	class Meta:
		model = models.HashTag
		fields = [
		'name',
		]
		labels = {
        "name":"標籤",
    	}
    	
'''
HashTagInlineformset = forms.inlineformset_factory(
	models.Article,
	models.HashTag,
	max_num=1,
	fields = [
	'title',
	'content',
	'name',
	]
)
'''