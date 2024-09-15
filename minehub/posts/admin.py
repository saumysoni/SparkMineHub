# admin.py

from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image')  # Add 'image_preview' to display image thumbnail

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return 'No Image'

    image_preview.short_description = 'Image Preview'
