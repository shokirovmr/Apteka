from rest_framework import generics
from .models import Pill, Doctor, Category, Commentary, Entry
from .serializers import PillSerializer, DoctorSerializer, CategorySerializer, CommentarySerializer, EntrySerializer


class PillListCreateView(generics.ListAPIView):
    queryset = Pill.published_objects.all()
    serializer_class = PillSerializer


class PillDetailView(generics.RetrieveAPIView):
    queryset = Pill.published_objects.all()
    serializer_class = PillSerializer


class DoctorListCreateView(generics.ListAPIView):
    queryset = Doctor.published_objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.published_objects.all()
    serializer_class = DoctorSerializer


class CategoryListCreateView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentaryListCreateView(generics.ListCreateAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


class CommentaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


class EntryListCreateView(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
