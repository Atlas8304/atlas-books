from django.contrib import admin

from .models import Author, Genre, Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ("title", "isbn")
    list_display = ("title", "isbn", "description")


class AuthorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
