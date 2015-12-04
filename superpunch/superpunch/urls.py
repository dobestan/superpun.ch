from django.conf.urls import url, include
from django.contrib import admin

from tidbits.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include([
        url(r'^$', TidbitsListView.as_view(), name='list'),
        url(r'^(?P<slug>\w+)/$', TidbitsDetailView.as_view(), name='detail'),
    ], namespace='tidbits', app_name='tidbits'))
]
