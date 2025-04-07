from django.contrib import admin
from django.utils.safestring import SafeString, mark_safe
from django.templatetags.static import static
from .models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)


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


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
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

    def has_add_permission(self, request) -> bool:
        return Gender.objects.exists()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return (
            Author.objects.exists()
            and Tag.objects.exists()
            and Category.objects.exists()
        )
