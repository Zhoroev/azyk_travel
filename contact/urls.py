from django.urls import path

from .views import MessageViewSet, SocialMediaViewSet, ContactViewSet


urlpatterns = [
    path('message/', MessageViewSet.as_view({'post': 'create', })),
    path('contacts/', ContactViewSet.as_view({'get': 'list', })),
    path('contacts/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve', })),
    path('social_media/', SocialMediaViewSet.as_view({'get': 'list', })),
    path('social_media/<int:pk>/', SocialMediaViewSet.as_view({'get': 'retrieve', })),
]