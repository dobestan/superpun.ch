from celery import Task

from tidbits.models import Tidbit


class UpdateTidbitMetaTags(Task):

    def run(self, tidbit_id, *args, **kwargs):
        tidbit = Tidbit.objects.get(pk=tidbit_id)
        tidbit.update_meta_tags()
