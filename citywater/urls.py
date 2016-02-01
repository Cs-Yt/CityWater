"""citywater URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from index import views as index_views
from temp import views as temp_views

urlpatterns = [
    url(r'^$', index_views.index),
    url(r'^admin/$', admin.site.urls),
    url(r'^temp/([\w]{16})/$', temp_views.chart),
    url(r'^history/([\w]{16})/$', temp_views.history),
    url(r'^rttemp/list/$', temp_views.rtlist),
    url(r'^rttemp/([\w]{16})/(\d+)/$', temp_views.rttemp),
    url(r'^rtvdd/([\w]{16})/(\d+)/$', temp_views.rtvdd),
    url(r'^rttemp/([\w]{16})/all/$', temp_views.rttemp_all),
    url(r'^rtvdd/([\w]{16})/all/$', temp_views.rtvdd_all),
]
