from django.views.generic import View

from tidbits.models import Tidbit


class TidbitsBaseView(View):
    model = Tidbit

    def get_queryset(self):
        return super(TidbitsBaseView, self).get_queryset()\
            .filter(
                is_public=True,
                provider__is_public=True,
            )
