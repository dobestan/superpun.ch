from django.core.management.base import BaseCommand

from tidbits.tasks.feed import UpdateProviderFeedTask


class Command(BaseCommand):
    help = "Update Tidbits from all provider."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        task = UpdateProviderFeedTask()
        task.delay()
