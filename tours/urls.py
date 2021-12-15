from django.urls import path
from .views import TourViewSet, QuestionViewSet, CategoryViewSet


urlpatterns = [
    path('tours/', TourViewSet.as_view({'get': 'list', })),
    path('tours/<int:pk>/', TourViewSet.as_view({'get': 'retrieve', })),
    path('questions/', QuestionViewSet.as_view({'get': 'list', })),
    path('questions/<int:pk>/', QuestionViewSet.as_view({'get': 'retrieve', })),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', })),
    path('categories/', CategoryViewSet.as_view({'get': 'list', })),
]


