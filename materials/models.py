from django.db import models

feature_30.2
from config.settings import AUTH_USER_MODEL

class Course(models.Model):
    """ Модель курса """

    course_name = models.CharField(max_length=50, verbose_name="Название курса")
    images = models.ImageField(
        upload_to="course/images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию",
    )
    course_description = models.TextField(max_length=250, verbose_name="Описание")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.course_name} {self.course_description}"


class Lesson(models.Model):
    """ Модель урока """

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

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.lesson_name} {self.lesson_description}"

# Create your models here.
develop
