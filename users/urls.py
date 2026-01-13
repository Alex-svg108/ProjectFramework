from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import PaymentsViewSet, PaymentCreateAPIView, UserCreateAPIView


app_name = "users"

router = SimpleRouter()
router.register(r'payments', PaymentsViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
]

urlpatterns += router.urls
