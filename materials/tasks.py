from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from config import settings
from django.core.mail import send_mail

from users.models import User

@shared_task
def subscription_for_course_updates(course, email):
    send_mail(
        subject="Обновление курса",
        message=f"Материалы курса {course} обновлены!",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )

@shared_task
def verification_user():
    now = timezone.now()
    users = User.objects.filter(
        last_login__lte=now - timedelta(days=30), is_active=True
    )
    for user in users:
        user.is_active = False
        user.save()
