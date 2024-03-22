from django.urls import path
from .views import *

urlpatterns = [
    path("", get_courses, name="get_courses"),
    path("latest/", latest_courses, name="latest_courses"),
    path("get_categories/", get_categories, name="get_categories"),
    path("<slug:slug>/", get_course_detail, name="get_course_detail"),
    path(
        "<slug:course_slug>/<slug:lesson_slug>/",
        create_comment,
        name="create_comment",
    ),
    path(
        "<slug:course_slug>/<slug:lesson_slug>/get-comments/",
        get_comments,
        name="get_comments",
    ),
]
