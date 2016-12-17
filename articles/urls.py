from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.article_list, name='list'),
	url(r'^tag/(?P<slug>[-\w]+)/$', views.tagged, name='tagged'),
	url(r'(?P<pk>\d+)/$', views.article_detail, name='detail'),
	url(r'(?P<pk>\d+)/delete$', views.article_delete, name='delete'),
	url(r'(?P<pk>\d+)/comment_delete$', views.comment_delete, name='comment_delete'),
	url(r'^create/$', views.create, name='create'),
	url(r'(?P<pk>\d+)/create_comment/$', views.create_comment, name='create_comment'),
	url(r'(?P<article_pk>\d+)/edit_article/$', views.article_edit, name='article_edit'),
]