"""mopple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mopple.views.index', name='index'),
    url(r'^login/$', 'mopple.views.login'),
    url(r'^user/$', 'mopple.views.user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', 'mopple.views.user_detail'),
    url(r'^profile/$', 'mopple.views.profile_list'),
    url(r'^profile/(?P<pk>[0-9]+)/$', 'mopple.views.profile_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)