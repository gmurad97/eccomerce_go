from django.db import models
from django.urls import reverse 
from .author import Author
from .tag import Tag
from .category import Category


class Product(models.Model):
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
        return reverse("product:product_detail",kwargs={"id": self.id})

    def get_final_price(self) -> float:
        price_with_tax = self.price + self.tax_price
        return price_with_tax - (price_with_tax * (self.discount / 100))

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
