from django.urls import path
from .views import TourViewSet, QuestionViewSet, CategoryViewSet, TopTourViewSet


urlpatterns = [
    path('tours/', TourViewSet.as_view({'get': 'list', })),
    path('tours/<int:pk>/', TourViewSet.as_view({'get': 'retrieve', })),
    path('top_tours/', TopTourViewSet.as_view({'get': 'list', })),
    path('top_tours/<int:pk>/', TopTourViewSet.as_view({'get': 'retrieve', })),
    path('questions/', QuestionViewSet.as_view({'get': 'list', })),
    path('questions/<int:pk>/', QuestionViewSet.as_view({'get': 'retrieve', })),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', })),
    path('categories/', CategoryViewSet.as_view({'get': 'list', })),
]


