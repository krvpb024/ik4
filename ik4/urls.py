"""ik4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from .views import index, logout, register
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    password_reset, 
    password_reset_done,
    password_reset_confirm, 
    password_reset_complete,
    # these are the two new imports
    password_change,
    password_change_done,
)


urlpatterns = [
	url(r'^article/', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^accounts/login/$',login),
	url(r'^accounts/logout/$',logout),
	url(r'^index/$',index),
	url(r'^accounts/register/$',register),
	url(r'^profile_view/(?P<author_id>\w+)/$', views.user_profile, name='user_profile'),
	url(r'^profile_edit/(?P<user_name>\w+)/$', views.edit_profile, name='edit_profile'),
    url(r'^password/change/(?P<user_name>\w+)/$', views.password_change, name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done, 
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
]



urlpatterns += staticfiles_urlpatterns()