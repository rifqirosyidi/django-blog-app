from django.contrib import admin
from .models import Post


# Customize admin site
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'updated', 'timestamp']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']
    # list_display_links = ['updated']  # Focused Link

    class Meta:
        model = Post


# Register your models here.
admin.site.register(Post, PostModelAdmin)
