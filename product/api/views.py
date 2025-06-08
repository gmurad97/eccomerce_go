from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response

name_param = openapi.Parameter(
    "name",
    openapi.IN_QUERY,
    description="Имя пользователя",
    type=openapi.TYPE_STRING,
)


class HelloView(APIView):
    @swagger_auto_schema(
        manual_parameters=[name_param],
        operation_description="Приветственный эндпоинт, который возвращает приветствие с именем из query",
        responses={
            200: openapi.Response(
                "Успешный ответ",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Приветственное сообщение",
                        )
                    },
                ),
            )
        },
    )
    def get(self, request):
        name = request.GET.get("name", "гость")
        return Response({"message": f"Hello, {name}!"})
