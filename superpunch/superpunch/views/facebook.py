from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.base import RedirectView


class FacebookPageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        current_site = get_current_site(self.request)
        return current_site.site_profile.facebook_page_url


class FacebookMessageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        current_site = get_current_site(self.request)
        return current_site.site_profile.facebook_message_url
