from rest_framework import serializers
from .models import Category, Course, Lesson, Comment, Category


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
        )


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "long_description",
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
