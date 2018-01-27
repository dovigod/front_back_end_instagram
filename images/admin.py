from django.contrib import admin
from . import models
# Register your models here.


class Image__admin(admin.ModelAdmin):

    ordering = (
        'caption',
        'created_by',
    )

    list_display = (
        'location',
        'caption',
        'created_by',
        'updated_at',
        'created_at',
    )

    list_display_links = (
        'caption',
        'location',
    )

    search_fields = (
        'location',
    )

    list_filter = (
        'created_at',
        'location',
    )


admin.site.register(models.Image, Image__admin)
admin.site.register(models.Comment)
admin.site.register(models.Like)
