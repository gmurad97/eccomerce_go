from django.contrib import admin
from django.utils.safestring import SafeString, mark_safe
from django.templatetags.static import static
from ..models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "fullname_tag",
        "age",
        "birthday",
        "status",
    )
    list_display_links = ("fullname_tag",)
    list_editable = ("status",)

    @admin.display(description="Full Name")
    def fullname_tag(self, obj) -> str:
        return f"{obj.name} {obj.surname}"

    @admin.display(description="Image")
    def image_tag(self, obj) -> SafeString:
        if obj.image:
            return mark_safe(
                f"<a href='{obj.image.url}' data-lity><img class='preview__image' src='{obj.image.url}' alt='Preview'></a>"
            )
        else:
            return mark_safe(
                f"<a href='{static("admin/img/no_image.png")}' data-lity><img class='preview__image' src='{static("admin/img/no_image.png")}' alt='Preview'></a>"
            )

    def has_add_permission(self, request) -> bool:
        return Gender.objects.exists()

    class Media:
        css = {
            "all": ("admin/plugins/lity@2.4.1/lity.min.css",),
        }
        js = ("admin/plugins/lity@2.4.1/lity.min.js",)
