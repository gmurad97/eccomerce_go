from django.http import JsonResponse
from django.views import View
import razorpay
from typing import Any

RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_secret"

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


class CreateOrderView(View):
    def post(self, request, *args: Any, **kwargs: Any) -> JsonResponse:
        amount = 50000  # 500.00 INR
        order_data = {
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1,
        }
        order = client.order.create(data=order_data)
        return JsonResponse(order)
