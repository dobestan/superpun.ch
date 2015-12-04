from django.views.generic import View

from tidbits.models import Tidbit


class TidbitsBaseView(View):
    model = Tidbit
