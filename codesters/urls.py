from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from resources.models import Resource, Topic
from profiles.models import UserProfile

from django.views.generic import RedirectView
from .views import *
from profiles.views import UserUpdateView, UserProfileUpdateView
from .sitemaps import sitemaps

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='page_home'),
    url(r'^about/$', AboutView.as_view(), name='page_about'),
    url(r'^contact/$', ContactView.as_view(), name='page_contact'),
    url(r'^guidelines/$', GuidelinesView.as_view(), name='page_guidelines'),
    url(r'^explore/$', explore_home, name='explore_home'),
    url(r'^admin/$', RedirectView.as_view(url='/', permanent=True)),
    url(r'^explore/resource/all/$', RecentResourceListView.as_view(), name='explore_recent_resources'),
    url(r'^explore/domain/all/$', PopularDomainListView.as_view(), name='explore_all_domains'),
    url(r'^explore/topic/all/$', PopularTopicListView.as_view(), name='explore_all_topics'),
    url(r'^accounts/settings/core/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^accounts/settings/info/$', UserProfileUpdateView.as_view(), name='userprofile_update'),
)

urlpatterns += patterns('',
    url(r'^manage/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^resource/', include('resources.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^search/', include('haystack.urls')),
)


urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
