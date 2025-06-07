from django.urls import path
from .views import HelloView

urlpatterns = [
    path("products/", HelloView.as_view(), name="product-list"),
]
