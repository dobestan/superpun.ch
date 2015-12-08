from django.contrib import admin

from multisites.models import SiteProfile


@admin.register(SiteProfile)
class SiteProfileModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'site',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'site__name',
        'site__domain',
    )

    readonly_fields = (
        'site',

        'created_at',
        'updated_at',
    )
