from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pradeepchand.views.home', name='home'),
    # url(r'^pradeepchand/', include('pradeepchand.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='polls'), name="go-to-polls"),
)
