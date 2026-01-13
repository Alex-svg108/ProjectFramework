from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from users.models import Payments, User
from users.serializers import PaymentSerializer, UserSerializer

feature_30.2
class PaymentsViewSet(ModelViewSet):
    """ API для работы с платежами """

    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['payment_course', 'payment_lesson', 'payment_method']  # поля для фильтрации
    search_fields = ['payment_course', 'payment_lesson', 'payment_method']  # поля для фильтрации
    ordering_fields = ['payment_date']  # поле для сортировки

class PaymentCreateAPIView(CreateAPIView):
    """ API для создания платежа """

    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

class UserCreateAPIView(CreateAPIView):
    """ API для создания пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()

# Create your views here.
develop
