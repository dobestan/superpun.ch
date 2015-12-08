from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.base import RedirectView


class FacebookPageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        current_site = get_current_site(self.request)

        return "https://www.facebook.com/{facebook_page_slug}".format(
            facebook_page_slug=current_site.site_profile.facebook_page_slug,
        )


class FacebookMessageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        current_site = get_current_site(self.request)

        return "https://m.facebook.com/messages/thread/{facebook_page_id}".format(
            facebook_page_id=current_site.site_profile.facebook_page_id,
        )
