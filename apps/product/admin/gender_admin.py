from django.contrib import admin
from ..models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
