from django.db import models
from django.contrib.sites.models import Site

from tidbits.utils.image import meta_image_upload_to


class TidbitManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'provider',
            'provider__site',
            'provider__site__siteprofile',
        )

    def public(self):
        return self.filter(
            is_public=True,
            provider__is_public=True,
            is_meta_crawled=True,
        )


class Tidbit(models.Model):

    site = models.ForeignKey(
        Site,
        blank=True,
        null=True,
    )

    provider = models.ForeignKey(
        'Provider',
        blank=True,
        null=True,
    )

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )

    # RSS/Atom Feed
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

    # Web Crawling
    # The MOST IMPORTANT information about tidbits are "META TAGS".
    original_html = models.TextField(blank=True, null=True, )

    meta_title = models.CharField(max_length=128, blank=True, null=True, )
    meta_description = models.TextField(blank=True, null=True, )
    meta_keywords = models.CharField(max_length=256, blank=True, null=True, )
    meta_image_url = models.URLField(blank=True, null=True, )
    meta_image = models.ImageField(
        upload_to=meta_image_upload_to,
        blank=True,
        null=True,
    )
    is_meta_crawled = models.BooleanField(
        default=False,
    )

    is_public = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TidbitManager()

    class Meta:
        ordering = ['-created_at', ]
        get_latest_by = 'created_at'
        unique_together = (
            ('provider', 'title', ),
        )

    def __str__(self):
        return "{provider_name}: {title}".format(
            provider_name=self.provider.name,
            title=self.title,
        )

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

    def update_meta_tags(self):
        self.crawl()
        self.parse_meta_tags()
        self.update_meta_image()

        self.is_meta_crawled = True
        self.is_public = True
        self.save()

    def crawl(self):
        """Crawl original_html from original_url."""
        import requests

        response = requests.get(self.original_url)

        self.original_html = response.text
        self.save()

    def parse_meta_tags(self):
        """Parse meta tags from original_html."""
        from tidbits.utils.parser import MetaTagParser

        parser = MetaTagParser(self.original_html)
        meta_tags = parser.run()

        self.meta_title = meta_tags.get('title', None)
        self.meta_description = meta_tags.get('description', None)
        self.meta_keywords = meta_tags.get('keywords', None)
        self.meta_image_url = meta_tags.get('image_url', None)
        self.save()

    def update_meta_image(self):
        from tidbits.utils.crawler import ImageCrawler

        self.meta_image = ImageCrawler.run(self.meta_image_url)
        self.save()
