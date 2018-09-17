from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin

admin.autodiscover()

import pydsp.views

# Examples:
# url(r'^$', 'server.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', pydsp.views.index, name='index'),

    url(r'^contact', pydsp.views.contact, name='contact'),
    url(r'^about', pydsp.views.about, name='about'),
    url(r'^linear_conv', pydsp.views.linear_conv, name='linear_conv'),
    url(r'^circular_conv', pydsp.views.circular_conv, name='circular_conv'),
    url(r'^imp_respf', pydsp.views.imp_respf, name='imp_respf'),
    url(r'^imp_resps', pydsp.views.imp_resps, name='imp_resps'),
    url(r'^ndft', pydsp.views.ndft, name='ndft'),
    url(r'^dft_idft', pydsp.views.dft_idft, name='dft_idft'),
    url(r'^auto_corr', pydsp.views.auto_corr, name='auto_corr'),
    url(r'^cross_corr', pydsp.views.cross_corr, name='cross_corr'),
    url(r'^sampling', pydsp.views.sampling, name='sampling'),
    # url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
