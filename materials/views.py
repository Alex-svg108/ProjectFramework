from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

feature_30.2
from materials.models import Course, Lesson
from materials.serializer import CourseSerializer, LessonSerializer, CourseDetailSerializer

class CourseViewSet(ModelViewSet):
    """ API для работы с курсами """

    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

class LessonCreateAPIView(CreateAPIView):
    """ API для создания урока """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonListAPIView(ListAPIView):
    """ API для получения списка уроков """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveAPIView(RetrieveAPIView):
    """ API для получения урока по ID """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonUpdateAPIView(UpdateAPIView):
    """ API для обновления урока """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDestroyAPIView(DestroyAPIView):
    """ API для удаления урока """

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# Create your views here.
develop
