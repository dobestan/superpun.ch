from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from tidbits.views import *
from superpunch.views import *


urlpatterns = [
    url(r'^superadmin/', admin.site.urls),

    url(r'^', include([
        url(r'^facebook/$', FacebookPageRedirectView.as_view(), name='page'),
        url(r'^facebook/message/$', FacebookMessageRedirectView.as_view(), name='message'),

        url(r'^contact/$', FacebookMessageRedirectView.as_view(), name='contact'),
    ], namespace='facebook')),

    url(r'^', include([
        # url(r'^$', TidbitsListView.as_view(), name='list'),
        url(r'^$', FacebookPageRedirectView.as_view(), name='list'),
        url(r'^(?P<slug>\w+)/$', TidbitsDetailView.as_view(), name='detail'),
    ], namespace='tidbits', app_name='tidbits')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
