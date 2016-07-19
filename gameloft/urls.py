"""gameloft URL Configuration

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
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^eva/$', views.eva, name="eva"),
    url(r'^pandora/$', views.pandora, name="pandora"),
    # Write all API here
    # url(r'^/pandora', views.pandora, name="pandora"),
    # url(r'^/janus', views.janus, name="janus"),
    # url(r'^/seshat', views.seshat, name="seshat"),
    # url(r'^/herms', views.herms, name="herms"),
    # url(r'^/olympus', views.olympus, name="olympus"),
]
