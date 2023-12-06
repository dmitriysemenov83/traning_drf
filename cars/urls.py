from django.urls import path

from cars.apps import CarsConfig
from cars.views import CarCreateAPIView, CarListAPIView, CarRetrieveAPIView, CarUpdateAPIView, CarDestroyAPIView

app_name = CarsConfig.name


urlpatterns = [
    path('', CarListAPIView.as_view(), name='cars_list'),
    path('create/', CarCreateAPIView.as_view(), name='car-create'),
    path('retrieve/<int:pk>/', CarRetrieveAPIView.as_view(), name='car-retrieve'),
    path('update/<int:pk>/', CarUpdateAPIView.as_view(), name='car-update'),
    path('delete/<int:pk>/', CarDestroyAPIView.as_view(), name='car-delete'),
]
