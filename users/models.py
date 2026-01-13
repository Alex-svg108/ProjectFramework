from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

class User(AbstractUser):
    """ Модель пользователя """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Введите название города",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

class Payments(models.Model):
    """ Модель платежи """

    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, verbose_name="Кто произвел оплату")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')
    payment_course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Оплаченный курс")
    payment_lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Оплаченный урок")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость покупки")
    PAYMENT_METHODS = [
        ('cash', 'Наличные'),
        ('bank_transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, verbose_name='Способ оплаты')

    def __str__(self):
        return f"Payment {self.payment_date}: {self.payment_amount} {self.payment_method}"


