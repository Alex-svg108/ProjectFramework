from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

feature_32.1
from materials.models import Course, Lesson, Subscription
from users.models import User

class CourseTestCase(APITestCase):
    """ Тест для управления курсами """

    def setUp(self):
        self.user = User.objects.create(email="post@mail.ru")
        self.course = Course.objects.create(course_name="Django", course_description="как использовать ViewSet", owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name="Вьюсеты", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(data.get("course_name"), self.course.course_name)

    def test_course_create(self):
        url = reverse("materials:course-list")
        data = {"course_name": "Generic2", "course_description": "фреймворк"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        data = {"course_name": "Generic2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("course_name"), "Generic2"
        )


class LessonTestCase(APITestCase):
    """ Тест для управления уроками """

    def setUp(self):
        self.user = User.objects.create(email='post@mail.ru')
        self.course = Course.objects.create(course_name="Django", course_description="как использовать ViewSet", owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name="Вьюсеты", course=self.course, owner=self.user, lesson_description='Знакомство с ViewSet')
        self.client.force_authenticate(user=self.user)


    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("lesson_name"), self.lesson.lesson_name)


    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "lesson_name": "лекция2",
            "lesson_description": "фреймворк2",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)


    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

class SubscriptionTestCase(APITestCase):
    """ Тест для управления подписками """

    def setUp(self):
        self.user = User.objects.create(email='post@mail.ru')
        self.course = Course.objects.create(course_name="Django", course_description="как использовать ViewSet", owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name="Вьюсеты", course=self.course, owner=self.user, lesson_description='Знакомство с ViewSet')
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('materials:course_subscription')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'подписка добавлена'}
        )

    def test_subscription_delete(self):
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('materials:course_subscription')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'подписка удалена'}
        )

# Create your tests here.
develop
