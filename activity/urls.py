from django.urls import path
from .views import *

urlpatterns = [
    path("get_active_courses/", get_active_courses, name="get_active_courses"),
    path(
        "track_started/<slug:course_slug>/<slug:lesson_slug>/",
        track_started,
        name="track_started",
    ),
    path(
        "mark_as_done/<slug:course_slug>/<slug:lesson_slug>/",
        mark_as_done,
        name="mark_as_done",
    ),
]
