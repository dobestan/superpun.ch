from django.db import models


class TidbitManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related('provider', )

    def public(self):
        return self.filter(
            is_public=True,
            provider__is_public=True,
        )


class Tidbit(models.Model):

    provider = models.ForeignKey(
        'Provider',
    )

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    original_url = models.URLField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='원문 주소',
    )
    title = models.CharField(
        max_length=128,
        verbose_name='제목',
    )
    content = models.TextField(
        verbose_name='본문',
    )
    author = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        verbose_name='작성자',
    )

    is_public = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TidbitManager()

    class Meta:
        ordering = ['-created_at', ]
        unique_together = (
            ('provider', 'title', ),
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse(
            'tidbits:detail',
            kwargs={'slug': self.hash_id, },
        )

    def _create_hash_id(self):
        from tidbits.utils.hashids import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()
