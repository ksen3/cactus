from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'text', 'get_pic']
    save_on_top = True

    def get_pic(self, object):
        if object.photo:
            return mark_safe(f'<img src="{ object.photo.url }" width=50>')

    get_pic.short_description = "Миниатюра"

admin.site.register(MainContent, MainContentAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'email', 'text', 'created_at']
admin.site.register(Review, ReviewAdmin)