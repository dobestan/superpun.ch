from django.db import models
from django.contrib.sites.models import Site

from multisites.utils.image import default_meta_image_upload_to


class SiteProfileManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related('site')


class SiteProfile(models.Model):

    site = models.OneToOneField(
        Site,
        primary_key=True,
    )

    default_meta_title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    default_meta_description = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    default_meta_keywords = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    default_meta_image = models.ImageField(
        upload_to=default_meta_image_upload_to,
        blank=True,
        null=True,
        help_text="image/png, 1200px * 630px Recommended.",
    )

    facebook_app_id = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text='<a href="https://developers.facebook.com/" target="_blank">Facebook Developers</a>'
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

    google_analytics_tracking_id = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text='<a href="http://www.google.com/analytics/" target="_blank">Google Analytics</a>'
    )

    naver_site_verification = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        help_text='<a href="http://webmastertool.naver.com/" target="_blank">네이버 웹마스터도구</a>'
    )
    naver_analytics_tracking_id = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text='<a href="http://analytics.naver.com/" target="_blank">네이버 애널리틱스</a>'
    )

    ascii_art = models.TextField(
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

    @property
    def facebook_page_url(self):
        return "https://www.facebook.com/{facebook_page_slug}/".format(
            facebook_page_slug=self.facebook_page_slug,
        )

    @property
    def facebook_message_url(self):
        return "https://m.facebook.com/messages/thread/{facebook_page_id}/".format(
            facebook_page_id=self.facebook_page_id,
        )

    @property
    def facebook_page_profile_image_url(self):
        return "https://graph.facebook.com/{graph_api_version}/{facebook_page_id}/picture/".format(
            graph_api_version='v2.5',
            facebook_page_id=self.facebook_page_id,
        )
