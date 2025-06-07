"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import include, path
from product.views import page_not_found
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from product.api.views import HelloView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("product.urls", namespace="product")),
    path("api/v1/", include("product.api.urls")),
    path(
        "api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # получить токены
    path(
        "api/v1/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),  # обновить access
    path(
        "api/v1/hello/", HelloView.as_view(), name="hello"
    ),  # защищенный эндпоинт
]

handler404 = page_not_found


class MyAdminSite(AdminSite):
    AdminSite.site_header = "Панель управления"
    AdminSite.site_title = "Админка проекта"
    AdminSite.index_title = "Добро пожаловать"


admin_site = MyAdminSite(name="myadmin")

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
