from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Vote.myapp.views.home', name='home'),
	url(r'^home', 'Vote.myapp.views.home', name='home')
    url(r'^contact', 'Vote.myapp.views.contact', name='contact'),
    url(r'^about', 'Vote.myapp.views.about', name='about'),
    url(r'^linear_conv', 'Vote.myapp.views.linear_conv', name='linear_conv'),
    url(r'^circular_conv', 'Vote.myapp.views.circular_conv', name='circular_conv'),
    url(r'^imp_respf', 'Vote.myapp.views.imp_respf', name='imp_respf'),
    url(r'^imp_resps', 'Vote.myapp.views.imp_resps', name='imp_resps'),
    url(r'^ndft', 'Vote.myapp.views.ndft', name='ndft'),
    url(r'^dft_idft', 'Vote.myapp.views.dft_idft', name='dft_idft'),
    url(r'^auto_corr', 'Vote.myapp.views.auto_corr', name='auto_corr'),
    url(r'^cross_corr', 'Vote.myapp.views.cross_corr', name='cross_corr'),
    url(r'^sampling', 'Vote.myapp.views.sampling', name='sampling'),


    #url(r'^Vote/', include('Vote.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


