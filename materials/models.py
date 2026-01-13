from django.db import models

feature_32.1
from config.settings import AUTH_USER_MODEL

class Course(models.Model):
    """Модель курса"""

    course_name = models.CharField(max_length=50, verbose_name="Название курса")
    images = models.ImageField(
        upload_to="course/images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию",
    )
    course_description = models.TextField(max_length=250, verbose_name="Описание")
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.course_name} {self.course_description}"


class Lesson(models.Model):
    """Модель урока"""

    lesson_name = models.CharField(max_length=50, verbose_name="Название урока")
    images = models.ImageField(
        upload_to="lesson/images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию",
    )
    lesson_description = models.CharField(max_length=250, verbose_name="Описание")
    video = models.URLField(blank=True, null=True, verbose_name="Видео")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Название курса",
        related_name="lessons",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.lesson_name} {self.lesson_description}"


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    sign_of_subscription = models.BooleanField(
        default=False, verbose_name="Признак подписки"
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):

        return f"{self.user}: {self.course}"

# Create your models here.
develop
