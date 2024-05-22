from rest_framework import generics
from .models import Pill, Doctor, Category
from .serializers import PillSerializer, DoctorSerializer, CategorySerializer


class PillListCreateView(generics.ListCreateAPIView):
    queryset = Pill.published_objects.all()
    serializer_class = PillSerializer


class PillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pill.published_objects.all()
    serializer_class = PillSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.published_objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.published_objects.all()
    serializer_class = DoctorSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
