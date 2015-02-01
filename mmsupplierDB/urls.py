from django.conf.urls import patterns, url

from mmsupplierDB import views

urlpatterns = patterns('',
    url(r'^add_external_company/$', views.add_external_company, name='add_external_company'),
    url(r'^list_external_companies/$', views.list_external_companies, name='list_external_companies'),
    # url(r'^list_activity_sheets_by_date/$', views.list_activity_sheets_by_date, name='list_activity_sheets_by_date'),
    # url(r'^create_tree/$', views.create_tree, name='create_tree'),
    # url(r'^update_activity/(\d+)$', views.update_activity, name='update_activity'),
    # url(r'^$', views.index, name='index'),
)