from rest_framework import serializers
from .models import Tour, TourPhoto, Program, Category, DatePrice, Accommodation, Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'image', 'tour', ]


class AccommodationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accommodation
        fields = ['id', 'location', 'night', 'body', ]


class DatePriceSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%d-%m-%Y")
    end = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = DatePrice
        fields = ['id', 'start', 'end', 'min_people', 'max_people', 'status', 'price',]


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ['id', 'name', 'body', 'placement', 'nutrition', 'day', ]


class TourPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourPhoto
        fields = ['id', 'name', 'image']


class TourSerializer(serializers.ModelSerializer):
    photos = TourPhotoSerializer(many=True, read_only=True)
    programs = ProgramSerializer(many=True, read_only=True)
    accommodation = AccommodationSerializer(many=True, read_only=True)
    date_prices = DatePriceSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = ['id', 'name', 'body', 'category', 'included', 'excluded', 'draft',
                  'day', 'photos', 'accommodation', 'date_prices', 'programs', 'questions']


class TourListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['id', 'name', 'body', 'category', 'draft', 'day', ]


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name',]


class CategorySerializer(serializers.ModelSerializer):
    tours = TourListSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = ['id', 'name', 'tours']
