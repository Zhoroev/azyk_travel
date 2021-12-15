from django.urls import path
from .views import EmployeeViewSet


urlpatterns = [
    path('employees/', EmployeeViewSet.as_view({'get': 'list', })),
    path('employees/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', })),
]