from django.contrib import admin
from ..models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
