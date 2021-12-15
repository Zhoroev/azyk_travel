from django.urls import path
from .views import PlaceViewSet


urlpatterns = [
    path('places/', PlaceViewSet.as_view({'get': 'list', })),
    path('places/<int:pk>/', PlaceViewSet.as_view({'get': 'retrieve', })),
]