from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'battlePyServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^battle/(?P<player1>\w+)/(?P<player2>\w+)/$', 'api.views.battle', name='battle'),
    url(r'^upload/$', 'api.views.upload', name='upload'),
 

]
