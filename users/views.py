from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from users.models import Payments, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session

class PaymentsViewSet(ModelViewSet):
    """API для работы с платежами"""

    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        "payment_course",
        "payment_lesson",
        "payment_method",
    ]  # поля для фильтрации
    search_fields = [
        "payment_course",
        "payment_lesson",
        "payment_method",
    ]  # поля для фильтрации
    ordering_fields = ["payment_date"]  # поле для сортировки


class PaymentCreateAPIView(CreateAPIView):
    """API для создания платежа"""

    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_stripe_product(payment)
        price = create_stripe_price(payment.payment_amount, product_id)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class UserCreateAPIView(CreateAPIView):
    """API для создания пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
