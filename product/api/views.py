from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.api.serializers import ProductListSerializer
from product.models import Product


@api_view(["GET"])
def index(request: HttpRequest):
    product = Product.objects.all()
    serializer = ProductListSerializer(product, many=True)
    print(serializer.data)
    return Response(serializer.data)
