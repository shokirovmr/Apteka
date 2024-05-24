from rest_framework import generics
from .models import Pill, Doctor, Category, Commentary, Entry
from .serializers import PillSerializer, DoctorSerializer, CategorySerializer, CommentarySerializer, EntrySerializer, \
    DiscountPillSerializer, SmallPillSerializer


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


class PopularPillsAPIView(generics.ListAPIView):
    serializer_class = SmallPillSerializer
    queryset = Pill.published_objects.filter(popular=True)


class LastPillsAPIView(generics.ListAPIView):
    serializer_class = PillSerializer
    queryset = Pill.published_objects.all()[:10]


class DiscountPillsAPIView(generics.ListAPIView):
    serializer_class = DiscountPillSerializer
    queryset = Pill.published_objects.all()

    def get_queryset(self):
        queryset = super(DiscountPillsAPIView, self).get_queryset()
        queryset = filter(lambda obj: obj.discount_price, queryset)
        return queryset


class RatingPillsAPIView(generics.ListAPIView):
    serializer_class = SmallPillSerializer

    def get_queryset(self):
        queryset = Pill.published_objects.all()
        return sorted(queryset, key=lambda obj: obj.rank, reverse=True)
