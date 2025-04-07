from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


from django.db.models import Q, F, Value, CharField, FloatField
from django.db.models.functions import Concat, Cast, Coalesce


def index(request) -> HttpResponse:
    context = {
        "page_title": "Home",
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

def error_404(request) -> HttpResponse:
    context = {
        "page_title": "page not found",
    }
    return render(request, "product/404.html", context)


# def index(request):
#     return render(request, "product/index.html")


# def allProducts(request):
#     return render(request, "product/shop-grid-3.html")


# def product_detail(request):
#     return render(request, "product/shop-single.html")


# & - AND // VE
# | - OR  // VE YA


# Product.objects.filter(
# +      Q(author_id=1)
# AND    &
# +      Q(author__name="Aytac")
# )

# Product.objects.filter(
# -      Q(author_id=1)
# OR     |
# +      Q(author__name="Aytac")
# )

# Product.objects.filter(Q(author_id=1) | Q(author__name="Aytac"))


# Annotate

# fullad = Author.objects.annotate(
#     full_name=Concat(
#         F("name"), Value(" "), F("surname"), Value(" -> "), Cast(F("age"), CharField())
#     )
# )


# from django.db.models import Q, F, Value, CharField, FloatField
# from django.db.models.functions import Concat, Cast, Coalesce

# cavab = Product.objects.annotate(
#     tax=Coalesce(F("tax_price"), 0, output_field=FloatField()),
#     discount=Coalesce(F("discount_price"), 0, output_field=FloatField())
# )


# from django.db.models import F, Value, FloatField
# from django.db.models.functions import Coalesce

# cavab = Product.objects.annotate(
#     tax=Coalesce(F("tax_price"), Value(0.0), output_field=FloatField()),
#     discount=Coalesce(F("discount_price"), Value(0.0), output_field=FloatField())
# )

# list(cavab.values("name", "tax", "discount"))
