from django.conf.urls import patterns, include, url
from django.contrib import admin
from user_admin.admin import user_admin_site
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(user_admin_site.urls)),
)