from django.contrib import admin
from . import models

# Register your models here.


class Pf_visualize(admin.ModelAdmin):
    order = (
        'avatar',
        'bio',
        'created_by',
    )

    display_list = (
        'created_by',
        'updated_at',
        'created_at',
    )

    search_field = ('created_by', )

    display_links = ('created_by')

    list_fillter = (
        'created_by',
        'created_at',
    )


admin.site.register(models.Profile, Pf_visualize)
