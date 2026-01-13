from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import ValidatorYouTube

class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Lesson. Возвращает количество уроков в курсе """

    courses = serializers.SerializerMethodField()
    validators = [ValidatorYouTube(field="video")]

    def get_courses(self, lesson):
        if hasattr(lesson, 'course') and lesson.course:
            return [lesson.course.course_name]
        return []

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Course. Возвращает список уроков в курсе """

    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

class CourseDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Course. Считает количество уроков в курсе """

    count_course_number_of_lessons = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    def get_count_course_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = ("course_name", "course_description", "count_course_number_of_lessons", "subscription")

class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор для управления подписками """

    class Meta:
        model = Subscription
        fields = ("sign_of_subscription",)
