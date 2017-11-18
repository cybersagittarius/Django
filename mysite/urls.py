#from django.conf.urls import patterns, include, url
from django.conf.urls import url, include
from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#)
urlpatterns=[
   # url(r'^admin/', include(admin.site.urls)),
     url(r'^admin/', admin.site.urls),
     url(r'', include('blog.urls')),
]
