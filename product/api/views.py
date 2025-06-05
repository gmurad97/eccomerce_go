from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.api.serializers import ProductListSerializer
from product.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import (
    PageNumberPagination,
)
from ..models import Product
from .serializers import ProductListSerializer


@api_view(["GET"])
def index(request: HttpRequest):
    product = Product.objects.all()
    serializer = ProductListSerializer(product, many=True)
    print(serializer.data)
    return Response(serializer.data)


class ProductListAPIView(APIView):

    def get(self, request):
        products = Product.objects.all().order_by("id")

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
