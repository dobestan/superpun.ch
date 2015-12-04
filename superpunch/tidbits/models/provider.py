from django.db import models


class ProviderManager(models.Manager):
    pass


class Provider(models.Model):

    name = models.CharField(
        max_length=16,
        unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
