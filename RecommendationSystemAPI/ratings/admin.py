from django.contrib import admin
from .models import MovieRating, BookRating


@admin.register(MovieRating)
class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "rating", "created_at")
    search_fields = ("user__username", "movie__title", "review")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("user", "movie")

    fieldsets = (
        (None, {"fields": ("user", "movie", "rating", "review")}),
        ("Дата создания", {"fields": ("created_at",), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at",)


@admin.register(BookRating)
class BookRatingAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "rating", "created_at")
    search_fields = ("user__username", "book__title", "review")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("user", "book")

    fieldsets = (
        (None, {"fields": ("user", "book", "rating", "review")}),
        ("Дата создания", {"fields": ("created_at",), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at",)