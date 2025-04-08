from django.db import models
from django.core.validators import FileExtensionValidator
from .gender import Gender


class Author(models.Model):
    image = models.FileField(
        upload_to="authors/",
        validators=[
            FileExtensionValidator(["png", "jpg", "jpeg", "svg", "webp"])
        ],
        blank=True,
        null=True,
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Gender",
    )
    name = models.CharField(
        max_length=300,
        verbose_name="Name",
    )
    surname = models.CharField(
        max_length=300,
        verbose_name="Surname",
    )
    age = models.PositiveIntegerField(
        verbose_name="Age",
    )
    birthday = models.DateField(
        verbose_name="Birthday",
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
        return f"{self.name}  {self.surname}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Author"
        verbose_name_plural = "Authors"
