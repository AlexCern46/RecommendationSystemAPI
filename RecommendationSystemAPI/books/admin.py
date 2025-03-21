from django.contrib import admin
from django.utils.html import format_html
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "release_year", "display_authors", "cover_preview")
    search_fields = ("title", "genre", "authors__name")  
    list_filter = ("release_year", "genre", "authors")  
    ordering = ("-release_year", "title")  
    autocomplete_fields = ("authors",)  
    readonly_fields = ("cover_preview",)  

    fieldsets = (
        (None, {"fields": ("title", "genre", "release_year")}),
        ("Авторы", {"fields": ("authors",)}),
        ("Описание", {"fields": ("description",)}),
        ("Обложка", {"fields": ("cover", "cover_preview")}),
    )

    def display_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    display_authors.short_description = "Авторы"

    def cover_preview(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.cover.url)
        return "Нет изображения"
    cover_preview.short_description = "Превью обложки"