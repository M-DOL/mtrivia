from django.conf.urls import include, url
from django.contrib import admin

from mcube.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^createuser/$', create_user),
    url(r'^newuser/$', new_user),
    url(r'^newuser/(?P<error>\d)/$', new_user),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^game/$', mtrivia),
    url(r'^calculator/', calculator),
    url(r'^leaderboard/', leaderboard),
    url(r'^openshift/', openshift),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<score>\w+)/$', update_leaderboard)
]
