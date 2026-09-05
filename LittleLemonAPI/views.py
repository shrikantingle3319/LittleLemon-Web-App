from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from .models import Category, MenuItem, Booking
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    BookingSerializer,
)


def home(request):
    return render(request, "index.html")


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]


class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer

    search_fields = [
        "title",
        "category__title",
    ]

    ordering_fields = [
        "title",
        "price",
        "featured",
    ]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get("category")
        featured = self.request.query_params.get("featured")

        if category:
            if category.isdigit():
                queryset = queryset.filter(
                    category_id=int(category)
                )
            else:
                queryset = queryset.filter(
                    category__title__iexact=category
                )

        if featured is not None:
            featured_value = featured.lower()

            if featured_value in ["true", "1"]:
                queryset = queryset.filter(featured=True)

            elif featured_value in ["false", "0"]:
                queryset = queryset.filter(featured=False)

        return queryset


class MenuItemDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = MenuItem.objects.select_related("category").all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        date = self.request.query_params.get("date")

        if date:
            queryset = queryset.filter(
                booking_date__date=date
            )

        return queryset


class BookingDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]