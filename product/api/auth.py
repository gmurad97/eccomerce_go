from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except InvalidToken:
            raise AuthenticationFailed(
                {
                    "error": "Ты кто такой? Проверь access токен.",
                    "code": "custom_token_error",
                }
            )
