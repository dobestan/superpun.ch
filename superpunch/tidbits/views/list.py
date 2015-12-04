from django.views.generic.list import ListView

from .base import TidbitsBaseView


class TidbitsListView(TidbitsBaseView, ListView):
    template_name = 'tidbits/list.html'
    context_object_name = 'tidbits'
