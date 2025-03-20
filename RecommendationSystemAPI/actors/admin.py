from django.contrib import admin

from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate")
    search_fields = ("name",)
    list_filter = ("birthdate",)
    ordering = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "birthdate")}),
        ("Дополнительно", {"fields": ("biography",), "classes": ("collapse",)}),
    )
