from rest_framework import serializers
from .models import Category, Course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
        )


class CourseListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "long_description",
            "categories",
        )
