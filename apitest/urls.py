"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from apitest.views import apis
from apitest.views import url_man
from apitest.views import host_env
from apitest.views import start

urlpatterns = [
    url(r'^urls/list/$', url_man.urlslist,name='urllist'),
    url(r'^urls/add/$', url_man.urladd,name='urladd'),
    url(r'^urls/edit/(\d+)/$', url_man.urledit,name='urledit'),
    url(r'^urls/del/(\d+)/$', url_man.urldel,name='urldel'),
    url(r'^api/list/$', apis.apilist,name='apilist'),
    url(r'^api/add/$', apis.apiadd,name='apiadd'),
    url(r'^api/edit/(\d+)/$', apis.apiedit,name='apiedit'),
    url(r'^api/del/(\d+)/$', apis.apidel,name='apidel'),
    url(r'^env/list/$', host_env.envlist, name='envlist'),
    url(r'^env/add/$', host_env.envadd, name='envadd'),
    url(r'^env/edit/(\d+)/$', host_env.envedit, name='envedit'),
    url(r'^env/del/(\d+)/$', host_env.envdel, name='envdel'),
    url(r'^start/$', start.start_test, name='start_test'),
    url(r'^result/$', start.test_result, name='test_result'),
]
