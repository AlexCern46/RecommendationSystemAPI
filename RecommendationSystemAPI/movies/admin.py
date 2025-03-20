from django.contrib import admin
from django.utils.html import format_html

from .models import Movie, MovieRating


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


@admin.register(MovieRating)
class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "rating", "created_at", "short_review")
    search_fields = ("movie__title", "user__username", "review")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("movie", "user")
    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {"fields": ("movie", "user", "rating")}),
        ("Отзыв", {"fields": ("review",)}),
        ("Дополнительно", {"fields": ("created_at",)}),
    )

    def short_review(self, obj):
        return obj.review[:50] + "..." if len(obj.review) > 50 else obj.review

    short_review.short_description = "Краткий отзыв"
