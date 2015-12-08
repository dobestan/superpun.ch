from django.db import models
from django.contrib.sites.models import Site


class SiteProfileManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related('site')


class SiteProfile(models.Model):

    site = models.OneToOneField(
        Site,
        primary_key=True,
    )

    facebook_page_id = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    facebook_page_slug = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SiteProfileManager()

    class Meta:
        db_table = 'multisites_site_profile'
        default_related_name = 'site_profile'

    def __str__(self):
        return self.site.__str__()
