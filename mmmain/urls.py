from django.conf.urls import patterns, url

from mmmain import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
)
