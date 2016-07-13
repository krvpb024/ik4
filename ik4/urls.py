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

urlpatterns = [
	url(r'^article/', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^accounts/login/$',login),
	url(r'^accounts/logout/$',logout),
	url(r'^index/$',index),
	url(r'^accounts/register/$',register),
]


urlpatterns += staticfiles_urlpatterns()