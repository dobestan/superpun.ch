from django.views.generic.detail import DetailView

from tidbits.models import Tidbit


class TidbitsDetailView(DetailView):
    model = Tidbit
    template_name = 'tidbits/detail.html'
    slug_field = 'hash_id'
    context_object_name = 'tidbit'
