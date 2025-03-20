from django.contrib import admin

from .models import UserMovieStatus


@admin.register(UserMovieStatus)
class UserMovieStatusAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "status")
    search_fields = ("user__username", "movie__title")
    list_filter = ("status",)
    ordering = ("user", "movie")
    autocomplete_fields = ("user", "movie")

    fieldsets = (
        (None, {"fields": ("user", "movie", "status")}),
    )
