from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Tour, Question, Category
from .serializers import (TourSerializer, TourListSerializer, QuestionSerializer, CategoryListSerializer, CategorySerializer )


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategorySerializer


class TourViewSet(ModelViewSet):
    queryset = Tour.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TourListSerializer
        else:
            return TourSerializer

    def get_queryset(self):
        return Tour.objects.all().filter(draft=False)


class TopTourViewSet(ModelViewSet):
    queryset = Tour.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TourListSerializer
        else:
            return TourSerializer

    def get_queryset(self):
        return Tour.objects.all().filter(is_top=True, draft=False)


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

