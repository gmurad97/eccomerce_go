from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name="Name",
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
        return reverse("product:tag_products", kwargs={"id": self.id})

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
