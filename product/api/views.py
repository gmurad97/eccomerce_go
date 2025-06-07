from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTQxMjM4OSwiaWF0IjoxNzQ5MzI1OTg5LCJqdGkiOiJkYjZjZmFjYTkyZTg0OWQyYTU1YTc4OTM4ZDEzNTEzZSIsInVzZXJfaWQiOjF9.Cjwzt_hsHqaqy_RmiV189hYx3KLIwoYzqKSlNYK4mo8"

        return Response(
            {"message": f"Hello, {request.user.username}!"},
            headers={"Authorization": f"Bearer {token}"},
        )
