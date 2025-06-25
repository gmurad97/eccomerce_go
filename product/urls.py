from django.urls import path
from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "product"

urlpatterns = [
    # ... другие пути
    path(
        "api/guarded/", views.MyProtectedView.as_view(), name="jwt_guarded"
    ),  # логин
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # логин
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # обновление токена
]
