from django.urls import path

from .views import ReviewViewSet


urlpatterns = [
    path('tours/<int:tour_id>/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create', })),
    path('tours/<int:tour_id>/reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                                                         'put': 'update',
                                                                         'patch': 'partial_update',
                                                                         'delete': 'destroy', })),

]
