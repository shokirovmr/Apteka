from django.urls import path
from .views import (PillListCreateView, PillDetailView, DoctorListCreateView,
                    DoctorDetailView, CategoryListCreateView, CategoryDetailView)

urlpatterns = [
    path('pills/', PillListCreateView.as_view(), name='pill-list'),
    path('pills/<int:pk>/', PillDetailView.as_view(), name='pill-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
