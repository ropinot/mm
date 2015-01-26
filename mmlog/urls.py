from django.conf.urls import patterns, url

from mmlog import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
    url(r'^add_activity_sheet/$', views.add_activity_sheet, name='add_activity_sheet'),
    url(r'^list_activity_sheets_by_date/$', views.list_activity_sheets_by_date, name='list_activity_sheets_by_date'),
    url(r'^create_tree/$', views.create_tree, name='create_tree'),
    url(r'^update_activity/$', views.update_activity, name='update_activity'),
    url(r'^$', views.index, name='index'),
)
