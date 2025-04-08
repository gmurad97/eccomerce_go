from django.contrib import admin
from django.utils.safestring import SafeString, mark_safe
from django.templatetags.static import static
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "icon_tag",
        "name",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)

    @admin.display(description="Icon")
    def icon_tag(self, obj) -> SafeString:
        if obj.icon:
            return mark_safe(
                f"<a href='{obj.icon.url}' data-lity><img class='preview__image' src='{obj.icon.url}' alt='Preview'></a>"
            )
        else:
            return mark_safe(
                f"<a href='{static("admin/img/no_image.png")}' data-lity><img class='preview__image' src='{static("admin/img/no_image.png")}' alt='Preview'></a>"
            )

    class Media:
        css = {
            "all": ("admin/plugins/lity@2.4.1/lity.min.css",),
        }
        js = ("admin/plugins/lity@2.4.1/lity.min.js",)
