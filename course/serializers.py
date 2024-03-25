from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Course, Lesson, Comment, Category, Quiz


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "slug",
        )


class CourseListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "slug",
            "get_image",
            "short_description",
            "categories",
        )


class CourseDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    created_by = UserSerializer(many=False)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "slug",
            "get_image",
            "short_description",
            "long_description",
            "categories",
            "created_by",
        )


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "slug",
            "type",
            "short_description",
            "long_description",
            "youtube_id",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "name",
            "content",
            "created_at",
        )


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "id",
            "course_id",
            "lesson_id",
            "question",
            "answer",
            "option1",
            "option2",
            "option3",
            "option4",
        )
