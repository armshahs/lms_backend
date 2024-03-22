from django.urls import path
from .views import *

urlpatterns = [
    path("", get_courses, name="get_courses"),
    path("<slug:slug>/", get_course_detail, name="get_course_detail"),
]
