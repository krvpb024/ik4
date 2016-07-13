from django.contrib import admin
from articles.models import Article, Comment, HashTag

# Register your models here.

class CommentInline(admin.StackedInline):
	model = Comment
	
class ArticleAdmin(admin.ModelAdmin):
	inlines = [CommentInline, ]
	
	def save_model(self, request, Article, form, change):
		if not change:
			Article.author = request.user
		Article.save()

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(HashTag)