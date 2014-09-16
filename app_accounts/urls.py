from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('app_accounts',
    url(r'^registration/$', 'views.registration', name='registration'),
    url(r'^registration_success/$', 'views.registration_success', name='registration_success'),
    url(r'^authentication/$', 'views.authentication', name='authentication'),
    url(r'^authentication_success/$', 'views.authentication_success', name='authentication_success'),    
    url(r'^logout/$', 'views.logout', name='logout'),    
)


