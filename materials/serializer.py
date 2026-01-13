from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """ Сериализатор для модели Lesson. Возвращает количество уроков в курсе """

    courses = SerializerMethodField()

    def get_courses(self, lesson):
        if hasattr(lesson, 'course') and lesson.course:
            return [lesson.course.course_name]
        return []

    class Meta:
        model = Lesson
        fields = "__all__"

class CourseSerializer(ModelSerializer):
    """ Сериализатор для модели Course. Возвращает список уроков в курсе """

    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

class CourseDetailSerializer(ModelSerializer):
    """ Сериализатор для модели Course. Считает количество уроков в курсе """

    count_course_number_of_lessons = SerializerMethodField()

    def get_count_course_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("course_name", "course_description", "count_course_number_of_lessons")