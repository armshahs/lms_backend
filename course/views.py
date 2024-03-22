from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)

from .serializers import (
    CourseListSerializer,
    CategorySerializer,
    CourseDetailSerializer,
    LessonListSerializer,
)
from .models import Course, Category, Lesson


# Create your views here.
@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    lessons = course.lessons.all()

    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(lessons, many=True)

    return Response(
        {"course": course_serializer.data, "lessons": lesson_serializer.data}
    )
