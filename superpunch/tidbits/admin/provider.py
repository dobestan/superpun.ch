from django.contrib import admin

from tidbits.models import Provider


@admin.register(Provider)
class ProviderModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
