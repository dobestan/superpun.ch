from django.contrib import admin

from tidbits.models import Tidbit


@admin.register(Tidbit)
class TidbitModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'provider',

        'title',
        'original_url',
        'hash_id',

        'is_public',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'provider',
        'is_public',
    )

    inlines = (
    )

    search_fields = (
        'title',
        'hash_id',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
