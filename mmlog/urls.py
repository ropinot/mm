from django.conf.urls import patterns, url

from mmlog import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
    url(r'^add_activity_sheet/$', views.add_activity_sheet, name='add_activity_sheet'),
    url(r'^list_activity_sheet/$', views.list_activity_sheet, name='list_activity_sheet'),
    url(r'^$', views.index, name='index'),
)
