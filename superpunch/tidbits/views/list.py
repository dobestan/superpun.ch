from django.views.generic.list import ListView

from tidbits.models import Tidbit


class TidbitsListView(ListView):
    model = Tidbit
    template_name = 'tidbits/list.html'
    context_object_name = 'tidbits'
