from django.db import models


class Gender(models.Model):
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

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Gender"
        verbose_name_plural = "Genders"
