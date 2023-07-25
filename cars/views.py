from django.shortcuts import render
from .models import Car
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import CarSerializer

# Create your views here.

class CarListView(ListCreateAPIView) :
    queryset = Car.objects.all()
    serializer_class= CarSerializer

class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class= CarSerializer

# class CarDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class= CarSerializer