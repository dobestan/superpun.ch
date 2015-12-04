from django.db import models

from .provider import Provider


class TidbitManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related('provider', )


class Tidbit(models.Model):

    provider = models.ForeignKey(
        Provider,
    )

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    title = models.CharField(
        max_length=128,
        verbose_name='제목',
    )
    content = models.TextField(
        verbose_name='본문',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]
        unique_together = (
            ('provider', 'title', ),
        )

    def __str__(self):
        return self.title

    def _create_hash_id(self):
        from tidbits.utils.hashids import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()
