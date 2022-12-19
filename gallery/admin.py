from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class PhotosAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'slug', 'get_pic', 'author', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['title', 'get_pic']
    list_editable = ['is_published']
    ordering = ['-updated_at']
    prepopulated_fields = {'slug': ['title']}
    save_on_top = True

    def get_pic(self, object):
        if object.photo:
            return mark_safe(f'<img src="{ object.photo.url }" width=50>')

    get_pic.short_description = "Миниатюра"

admin.site.register(Photos, PhotosAdmin)