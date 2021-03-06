from django.conf.urls import patterns, include, url
from blog.models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'markedwards.views.home', name='home'),
    # url(r'^markedwards/', include('markedwards.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   
    url(r'^$', 'markedwards.views.home', name="home"),
    url(r'^bio/', 'markedwards.views.bio'),
    url(r'^press/', 'markedwards.views.press'),
    url(r'^schedule/$', 'markedwards.views.schedule', name="schedule"),
    url(r'^schedule/past/$', 'markedwards.views.past_schedule', name="past_schedule"),
    url(r'^programmes/$', 'markedwards.views.programmes'),
    url(r'^programmes/goldbergs', 'markedwards.views.goldbergs'),
    url(r'^programmes/allemande', 'markedwards.views.allemande'),
    url(r'^programmes/titans', 'markedwards.views.titans'),
    url(r'^discography/', 'markedwards.views.discography'),
    url(r'^media/', 'markedwards.views.media'),
    url(r'^links/', 'markedwards.views.links'),
    url(r'^blog/', include ('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
