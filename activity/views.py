from django.shortcuts import render

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response

from .models import Activity
from course.serializers import CourseListSerializer
from course.models import Course, Lesson
from .serializers import *


# Create your views here.
@api_view(["GET"])
def get_active_courses(request):
    courses = []

    activities = request.user.activities.all()
    for activity in activities:
        if activity.status == activity.STARTED and activity.course not in courses:
            courses.append(activity.course)

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def track_started(request, course_slug, lesson_slug):
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.filter(course=course).get(slug=lesson_slug)

    if (
        Activity.objects.filter(
            created_by=request.user, course=course, lesson=lesson
        ).count()
        == 0
    ):
        activity = Activity.objects.create(
            course=course, lesson=lesson, created_by=request.user
        )
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    return Response({"message": "Activity already started. Cannot start again"})


@api_view(["POST"])
def mark_as_done(request, course_slug, lesson_slug):
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.filter(course=course).get(slug=lesson_slug)
    activity = Activity.objects.get(
        created_by=request.user, course=course, lesson=lesson
    )

    activity.status = Activity.DONE
    activity.save()

    serializer = ActivitySerializer(activity)

    return Response(serializer.data)
