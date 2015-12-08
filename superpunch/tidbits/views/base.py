from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import View

from tidbits.models import Tidbit


class TidbitsBaseView(View):
    model = Tidbit

    def get_queryset(self):

        current_site = get_current_site(self.request)

        return super(TidbitsBaseView, self).get_queryset()\
            .filter(
                is_public=True,
                is_meta_crawled=True,
                provider__site=current_site,
                provider__is_public=True,
        )
