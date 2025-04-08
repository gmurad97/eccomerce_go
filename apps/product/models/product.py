import math
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from .author import Author
from .tag import Tag
from .category import Category


class Product(models.Model):
    poster = models.FileField(
        upload_to="products/%Y/%m/%d/",
        validators=[
            FileExtensionValidator(["png", "jpg", "jpeg", "svg", "webp"]),
        ],
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(
        max_length=300,
        verbose_name="Name",
    )
    price = models.FloatField(
        verbose_name="Price",
    )
    tax_price = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Tax Price",
    )
    discount = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Discount",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Tag",
    )
    coupon = models.CharField(
        max_length=32,
        blank=True,
        null=True,
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
        return reverse("product:product_detail", kwargs={"id": self.id})

    def get_price_with_tax(self) -> float:
        return math.ceil((self.price + self.tax_price) * 100) / 100

    def get_final_price(self) -> float:
        price_with_discount = self.price - (self.price * (self.discount / 100))
        return math.ceil(price_with_discount * 100) / 100 + self.tax_price

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"
