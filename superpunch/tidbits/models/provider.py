from django.db import models


class ProviderManager(models.Manager):

    def public(self):
        return self.filter(is_public=True, )


class Provider(models.Model):

    name = models.CharField(
        max_length=16,
        unique=True,
    )

    feed_url = models.URLField(
        blank=True,
        null=True,
        unique=True,
    )

    is_public = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProviderManager()

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def update_tidbits(self):
        """Add/Update provider tidbits from a RSS/Atom feed."""
        import feedparser

        feed_result = feedparser.parse(self.feed_url)

        for item in feed_result.entries:

            tidbit, created = self.tidbit_set.get_or_create(
                original_url=item.id,
            )

            if created:
                tidbit.title = item.title
                tidbit.author = item.author
                tidbit.content = item.description
                tidbit.save()
