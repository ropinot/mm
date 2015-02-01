from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^index/$', include('mmlog.urls')),
    # url(r'^add_activity_sheet/$', include('mmlog.urls')),
    url(r'^$', include('mmmain.urls')),
    url(r'^mmlog/', include('mmlog.urls')),
    url(r'^mmmain/', include('mmmain.urls')),
    url(r'^mmsupplierDB/', include('mmsupplierDB.urls')),
    url(r'^mmreport/', include('mmreport.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # AGGIUNGERE UN URL PER GESTIRE LE RICHIESTE NON VALIDE
)
