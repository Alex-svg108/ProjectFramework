from rest_framework.serializers import ValidationError


class ValidatorYouTube:
    """Проверка на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = "http://youtube.com"
        if value.get("video"):
            if url not in value.get("video"):
                raise ValidationError("Необходимо присутствие ссылки на youtube.")
        return None
