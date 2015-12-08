from django.views.generic.base import RedirectView


class FacebookPageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        facebook_page_slug = 'superpunchkr'
        return "https://www.facebook.com/{facebook_page_slug}".format(
            facebook_page_slug=facebook_page_slug,
        )


class FacebookMessageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        facebook_page_id = '652793861490830'
        return "https://m.facebook.com/messages/thread/{facebook_page_id}".format(
            facebook_page_id=facebook_page_id,
        )
