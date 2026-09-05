from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    MenuItemListCreateView,
    MenuItemDetailView,
    BookingListCreateView,
    BookingDetailView,
)


urlpatterns = [
    path(
        "categories/",
        CategoryListCreateView.as_view(),
        name="category-list",
    ),

    path(
        "categories/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),

    path(
        "menu-items/",
        MenuItemListCreateView.as_view(),
        name="menu-item-list",
    ),

    path(
        "menu-items/<int:pk>/",
        MenuItemDetailView.as_view(),
        name="menu-item-detail",
    ),

    path(
        "bookings/",
        BookingListCreateView.as_view(),
        name="booking-list",
    ),

    path(
        "bookings/<int:pk>/",
        BookingDetailView.as_view(),
        name="booking-detail",
    ),
]