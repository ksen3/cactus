from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cat', 'title', 'get_pic', 'preview', 'author', 'updated_at', 'is_published']
    list_editable = ['is_published']
    ordering = ['-updated_at']
    prepopulated_fields = {'slug': ['title']}
    save_on_top = True

    def get_pic(self, object):
        if object.photo:
            return mark_safe(f'<img src="{ object.photo.url }" width=50>')

    get_pic.short_description = "Миниатюра"
admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}
admin.site.register(Category, CategoryAdmin)
