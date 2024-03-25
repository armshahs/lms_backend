from django.shortcuts import render
import uuid

from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)

from django.contrib.auth.models import User

from .serializers import (
    CourseListSerializer,
    CategorySerializer,
    CourseDetailSerializer,
    LessonListSerializer,
    CommentSerializer,
    QuizSerializer,
    UserSerializer,
)
from .models import Course, Category, Lesson, Comment


# Create your views here.


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_courses(request):

    # to get category_id as a query param in the request.
    category_id = request.GET.get("category_id", "")
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[str(category_id)])

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


# Show latest courses on the home page
@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def latest_courses(request):
    courses = Course.objects.all()[0:4]
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


@api_view(["POST"])
def create_comment(request, course_slug, lesson_slug):

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.filter(course=course).get(slug=lesson_slug)

    comment = Comment.objects.create(
        name=request.data.get("name"),
        content=request.data.get("content"),
        lesson=lesson,
        course=course,
        created_by=request.user,
    )

    serializer = CommentSerializer(comment)

    return Response(serializer.data)


@api_view(["GET"])
def get_comments(request, course_slug, lesson_slug):

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.filter(course=course).get(slug=lesson_slug)

    comments = lesson.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_quiz(request, course_slug, lesson_slug):
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.filter(course=course).get(slug=lesson_slug)

    quiz = lesson.quizzes.all()
    serializer = QuizSerializer(quiz, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_author_courses(request, user_id):
    author = User.objects.get(id=user_id)
    courses = author.courses.all()

    user_serializer = UserSerializer(author)
    courses_serializer = CourseListSerializer(courses, many=True)

    return Response(
        {"created_by": user_serializer.data, "courses": courses_serializer.data}
    )
