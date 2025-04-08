from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from .models import Category, Product


def index(request) -> HttpResponse:
    categories = Category.objects.annotate(products_count=Count("products"))
    products = Product.objects.all()

    context = {
        "page_title": "Home",
        "categories": categories,
        "products": products,
        "last_categories": categories[:12],
        "last_products": products[:5],
        "hot_products": products.filter(discount__gte=20)[:5],
        "low_price_products": products.filter(price__lte=35)[:5],
    }
    return render(request, "product/pages/index.html", context)


def home(request) -> HttpResponseRedirect:
    return redirect("product:home")


def product_list(request) -> HttpResponse:
    context = {
        "page_title": "Products",
    }
    return render(request, "product/product_list.html", context)


def product_detail(request, id) -> HttpResponse:
    context = {
        "page_title": "Product IDs",
    }
    return render(request, "product/product_detail.html", context)


def category_list(request) -> HttpResponse:
    context = {
        "page_title": "Categories",
    }
    return render(request, "category/category_list.html", context)


def category_detail(request, id) -> HttpResponse:
    context = {
        "page_title": "Category IDs",
    }
    return render(request, "category/category_detail.html", context)


def tag_list(request) -> HttpResponse:
    context = {
        "page_title": "Tags",
    }
    return render(request, "tag/tag_list.html", context)


def tag_products(request, id) -> HttpResponse:
    context = {
        "page_title": "Tags IDs",
    }
    return render(request, "tag/tag_products.html", context)


def author_list(request) -> HttpResponse:
    context = {
        "page_title": "Authors",
    }
    return render(request, "author/author_list.html", context)


def author_detail(request, id) -> HttpResponse:
    context = {
        "page_title": "Authors IDs",
    }
    return render(request, "author/tag_products.html", context)


def brand_list(request) -> HttpResponse:
    context = {
        "page_title": "Brands",
    }
    return render(request, "author/brand_list.html", context)


def brand_products(request, id) -> HttpResponse:
    context = {
        "page_title": "Brands IDs",
    }
    return render(request, "author/brand_products.html", context)


def faq(request) -> HttpResponse:
    context = {
        "page_title": "FAQ",
    }
    return render(request, "product/faq.html", context)


def about(request) -> HttpResponse:
    context = {
        "page_title": "About",
    }
    return render(request, "product/about.html", context)


def contacts(request) -> HttpResponse:
    context = {
        "page_title": "Contacts",
    }
    return render(request, "product/contacts.html", context)


def error_404(request, exception) -> HttpResponse:
    context = {
        "page_title": "page not found",
    }
    return render(request, "product/404.html", context)
