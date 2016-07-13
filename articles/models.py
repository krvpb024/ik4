from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(User)
	content = models.TextField()
	tags = TaggableManager()
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
		

		
class Comment(models.Model):
	author = models.ForeignKey(User)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	article = models.ForeignKey(Article)
	
	def __str__(self):
		return self.content
		

class HashTag(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.title
		
class HashTagRelationship(models.Model):
	article = models.ForeignKey(Article)
	hashtag = models.ForeignKey(HashTag)