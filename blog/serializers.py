from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'link', 'file', 'image', 'created_at', ]


class PostListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image', 'created_at', ]