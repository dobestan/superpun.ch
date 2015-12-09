from django.db.models.signals import pre_save
from django.dispatch import receiver

from tidbits.models.tidbit import Tidbit


@receiver(pre_save, sender=Tidbit)
def pre_save_tidbit(sender, instance, **kwargs):
    if instance.provider:
        instance.site = instance.provider.site
