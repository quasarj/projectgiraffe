from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'giraffe.views.index'),
    url(r'^newpassword/$', 'giraffe.views.newpassword_view'),
    url(r'^pass/(?P<pass_hash>\w+)/$', 'giraffe.views.pass_view'),
)
