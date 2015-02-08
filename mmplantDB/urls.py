from django.conf.urls import patterns, url

from mmplantDB import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get_children/(\d+)$', views.get_children, name='get_children'),

)
