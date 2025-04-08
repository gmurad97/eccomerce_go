from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Name",
    )
    icon = models.FileField(
        upload_to="categories/",
        validators=[
            FileExtensionValidator(["png", "jpg", "jpeg", "svg", "webp"])
        ],
        blank=False,
        null=False,
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Status",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("product:category_detail", kwargs={"id": self.id})

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"
