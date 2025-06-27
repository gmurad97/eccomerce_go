from datetime import datetime
from typing import cast
from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from .models import (
    Tag,
    Category,
    Gender,
    Author,
    ProductImage,
    Product,
    SaleProduct,
    NewCollection,
)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "full_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("full_name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = ("email", "full_name")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):  # type: ignore
    model = Tag
    list_display = ("name", "created_at_tag", "updated_at_tag", "status")
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("created_at_tag", "updated_at_tag")

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj: Tag) -> str:
        created_at = cast(datetime, obj.created_at)
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "icon_tag",
        "name",
        "link_tag",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("icon_tag", "created_at_tag", "updated_at_tag")

    @admin.display(description="Link")
    def link_tag(self, obj):
        return format_html(
            "<a href='{}' target='_blank'>🔗{}</a>",
            obj.get_absolute_url(),
            obj.name,
        )

    @admin.display(description="Şəkil")
    def icon_tag(self, obj):
        if obj.icon:
            return format_html(
                "<a href='{}' data-lity>"
                "<img src='{}' style='height: 48px; border-radius: 50%;' />"
                "</a>",
                obj.icon.url,
                obj.icon.url,
            )
        else:
            return format_html(
                f"<a href='{static('admin/assets/img/no_image.png')}' data-lity>"
                f"<img src='{static('admin/assets/img/no_image.png')}' style='height: 48px; border-radius: 50%;' />"
                f"</a>"
            )

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")

    class Media:
        css = {"all": ("admin/assets/plugins/lity@2.4.1/lity.min.css",)}
        js = ("admin/assets/plugins/lity@2.4.1/lity.min.js",)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at_tag", "updated_at_tag", "status")
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("created_at_tag", "updated_at_tag")

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "image_tag",
        "__str__",
        "gender",
        "age_tag",
        "birthday_tag",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    list_display_links = ("__str__",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("created_at_tag", "updated_at_tag")

    @admin.display(description="Şəkil")
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                "<a href='{}' data-lity>"
                "<img src='{}' style='height: 48px; border-radius: 50%;' />"
                "</a>",
                obj.image.url,
                obj.image.url,
            )
        else:
            return format_html(
                f"<a href='{static('admin/assets/img/no_image.png')}' data-lity>"
                f"<img src='{static('admin/assets/img/no_image.png')}' style='height: 48px; border-radius: 50%;' />"
                f"</a>"
            )

    @admin.display(description="Yaş")
    def age_tag(self, obj):
        return obj.get_age()

    @admin.display(description="Doğum Günü")
    def birthday_tag(self, obj):
        return obj.birthday.strftime("%d.%m.%Y")

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")

    class Media:
        css = {"all": ("admin/assets/plugins/lity@2.4.1/lity.min.css",)}
        js = ("admin/assets/plugins/lity@2.4.1/lity.min.js",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    min_num = 0
    max_num = 4
    fields = ("image_tag", "image")
    readonly_fields = ["image_tag"]

    @admin.display(description="Preview")
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                "<a href='{}' data-lity>"
                "<img src='{}' style='height: 48px; border-radius: 50%;' />"
                "</a>",
                obj.image.url,
                obj.image.url,
            )
        else:
            return format_html(
                f"<a href='{static('admin/assets/img/no_image.png')}' data-lity>"
                f"<img src='{static('admin/assets/img/no_image.png')}' style='height: 48px; border-radius: 50%;' />"
                f"</a>"
            )

    class Media:
        css = {"all": ("admin/assets/plugins/lity@2.4.1/lity.min.css",)}
        js = ("admin/assets/plugins/lity@2.4.1/lity.min.js",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "poster_tag",
        "name",
        "category",
        "author",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("created_at_tag", "updated_at_tag")

    inlines = (ProductImageInline,)

    @admin.display(description="Şəkil")
    def poster_tag(self, obj):
        if obj.poster:
            return format_html(
                "<a href='{}' data-lity>"
                "<img src='{}' style='height: 48px; border-radius: 50%;' />"
                "</a>",
                obj.poster.url,
                obj.poster.url,
            )
        else:
            return format_html(
                f"<a href='{static('admin/assets/img/no_image.png')}' data-lity>"
                f"<img src='{static('admin/assets/img/no_image.png')}' style='height: 48px; border-radius: 50%;' />"
                f"</a>"
            )

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")

    class Media:
        css = {"all": ("admin/assets/plugins/lity@2.4.1/lity.min.css",)}
        js = ("admin/assets/plugins/lity@2.4.1/lity.min.js",)


@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    list_display = (
        "poster_tag",
        "name",
        "category",
        "author",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("created_at_tag", "updated_at_tag")

    inlines = (ProductImageInline,)

    @admin.display(description="Şəkil")
    def poster_tag(self, obj):
        if obj.poster:
            return format_html(
                "<a href='{}' data-lity>"
                "<img src='{}' style='height: 48px; border-radius: 50%;' />"
                "</a>",
                obj.poster.url,
                obj.poster.url,
            )
        else:
            return format_html(
                f"<a href='{static('admin/assets/img/no_image.png')}' data-lity>"
                f"<img src='{static('admin/assets/img/no_image.png')}' style='height: 48px; border-radius: 50%;' />"
                f"</a>"
            )

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(discount__gt=0)

    class Media:
        css = {"all": ("admin/assets/plugins/lity@2.4.1/lity.min.css",)}
        js = ("admin/assets/plugins/lity@2.4.1/lity.min.js",)


@admin.register(NewCollection)
class NewCollectionAdmin(admin.ModelAdmin):
    list_display = (
        "poster_tag",
        "name",
        "category",
        "author",
        "created_at_tag",
        "updated_at_tag",
        "status",
    )
    list_display_links = ("name",)
    list_editable = ("status",)
    list_per_page = 10
    readonly_fields = ("created_at_tag", "updated_at_tag")

    inlines = (ProductImageInline,)

    @admin.display(description="Şəkil")
    def poster_tag(self, obj):
        if obj.poster:
            return format_html(
                "<a href='{}' data-lity>"
                "<img src='{}' style='height: 48px; border-radius: 50%;' />"
                "</a>",
                obj.poster.url,
                obj.poster.url,
            )
        else:
            return format_html(
                f"<a href='{static('admin/assets/img/no_image.png')}' data-lity>"
                f"<img src='{static('admin/assets/img/no_image.png')}' style='height: 48px; border-radius: 50%;' />"
                f"</a>"
            )

    @admin.display(description="Yaranma tarixi")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%d.%m.%Y %H:%M")

    @admin.display(description="Yenilənmə tarixi")
    def updated_at_tag(self, obj):
        return obj.updated_at.strftime("%d.%m.%Y %H:%M")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(discount__isnull=True)

    class Media:
        css = {"all": ("admin/assets/plugins/lity@2.4.1/lity.min.css",)}
        js = ("admin/assets/plugins/lity@2.4.1/lity.min.js",)
