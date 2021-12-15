from rest_framework import serializers
from django.db import models
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='author.username')
    first_name = serializers.CharField(source='author.first_name', read_only=True)
    last_name = serializers.CharField(source='author.last_name', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'body', 'first_name', 'last_name', 'creation_date', ]
        read_only_fields = ['creation_date', ]
