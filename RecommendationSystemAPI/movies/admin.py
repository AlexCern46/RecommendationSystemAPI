from django.contrib import admin
from django.utils.html import format_html

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "genre", "display_directors", "display_actors", "poster_preview")
    search_fields = ("title", "genre", "directors__name", "actors__name")
    list_filter = ("release_year", "genre", "directors", "actors")
    ordering = ("-release_year", "title")
    autocomplete_fields = ("directors", "actors")
    readonly_fields = ("poster_preview",)

    fieldsets = (
        (None, {"fields": ("title", "genre", "release_year")}),
        ("Творческая команда", {"fields": ("directors", "actors")}),
        ("Дополнительно", {"fields": ("description", "poster", "poster_preview"), "classes": ("collapse",)}),
    )

    def display_directors(self, obj):
        return ", ".join([director.name for director in obj.directors.all()])

    display_directors.short_description = "Режиссеры"

    def display_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])

    display_actors.short_description = "Актеры"

    def poster_preview(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.poster.url)
        return "Нет изображения"

    poster_preview.short_description = "Превью постера"
