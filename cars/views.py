from rest_framework import generics

from cars.models import Car
from cars.serializers import CarSerializer


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer


class CarListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarDestroyAPIView(generics.DestroyAPIView):
    queryset = Car.objects.all()
