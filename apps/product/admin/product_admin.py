from django.contrib import admin
from django.utils.safestring import SafeString, mark_safe
from django.templatetags.static import static
from ..models import Product, Author, Tag, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "name",
        "author",
        "final_price_tag",
        "price",
        "tax_price",
        "discount",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)

    @admin.display(description="Image")
    def image_tag(self, obj) -> SafeString:
        if obj.poster:
            return mark_safe(
                f"<a href='{obj.poster.url}' data-lity><img class='preview__image' src='{obj.poster.url}' alt='Preview'></a>"
            )
        else:
            return mark_safe(
                f"<a href='{static("admin/img/no_image.png")}' data-lity><img class='preview__image' src='{static("admin/img/no_image.png")}' alt='Preview'></a>"
            )

    @admin.display(description="Final Price")
    def final_price_tag(self, obj) -> float:
        return obj.get_final_price()

    def has_add_permission(self, request) -> bool:
        return (
            Author.objects.exists()
            and Tag.objects.exists()
            and Category.objects.exists()
        )

    class Media:
        css = {
            "all": ("admin/plugins/lity@2.4.1/lity.min.css",),
        }
        js = ("admin/plugins/lity@2.4.1/lity.min.js",)
