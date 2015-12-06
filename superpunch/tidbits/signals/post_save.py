from django.db.models.signals import post_save
from django.dispatch import receiver

from tidbits.models import Tidbit


@receiver(post_save, sender=Tidbit)
def create_hash_id(sender, instance, created, **kwargs):
    if created:
        instance._create_hash_id()


@receiver(post_save, sender=Tidbit)
def update_meta_tags(sender, instance, created, **kwargs):
    from tidbits.tasks.meta import UpdateTidbitMetaTags

    if created:
        task = UpdateTidbitMetaTags()
        task.delay(instance.id)
