from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.home),
	
    path("products/", views.product_list, name="product_list"),
    path("products/<int:id>/", views.product_detail, name="product_detail"),
	

    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:id>/", views.category_detail, name="category_detail"),
	

    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:id>/", views.author_detail, name="author_detail"),
	
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/<int:id>/", views.tag_products, name="tag_products"),


    path("faq/", views.faq, name="faq"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
]
