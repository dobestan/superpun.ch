from django.views.generic.detail import DetailView

from .base import TidbitsBaseView


class TidbitsDetailView(TidbitsBaseView, DetailView):
    template_name = 'tidbits/detail.html'
    slug_field = 'hash_id'
    context_object_name = 'tidbit'
