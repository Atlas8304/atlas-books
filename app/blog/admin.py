from django.contrib import admin
from .models import BlogPost


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published_state", "creation_date")
    list_filter = ("published_state",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, PostAdmin)
