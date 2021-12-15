from rest_framework import serializers
from .models import Place, PlacePhoto


class PlacePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlacePhoto
        fields = ['id', 'name', 'image']


class PlaceSerializer(serializers.ModelSerializer):
    photos = PlacePhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'type', 'name', 'body', 'photos']