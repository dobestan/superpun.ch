from celery import Task

from tidbits.models import Provider


class UpdateProviderFeedDetailTask(Task):

    def run(self, provider_id, *args, **kwargs):
        provider = Provider.objects.get(pk=provider_id)
        provider.update_tidbits()


class UpdateProviderFeedTask(Task):

    def run(self, *args, **kwargs):
        task = UpdateProviderFeedDetailTask()

        for provider in Provider.objects.all():
            task.delay(provider.id)
