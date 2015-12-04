from django.db.models.signals import post_save
from django.dispatch import receiver

from tidbits.models import Tidbit


@receiver(post_save, sender=Tidbit)
def create_hash_id(sender, instance, created, **kwargs):
    if not instance.hash_id:
        instance._create_hash_id()
