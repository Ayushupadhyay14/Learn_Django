#
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'isbn',
                    'publication_date', 'created_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'created_at')
