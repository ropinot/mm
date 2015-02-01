from django.conf.urls import patterns, url

from mmreport import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'index/^$', views.index, name='index')
)