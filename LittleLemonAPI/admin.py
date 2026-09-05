from django.contrib import admin

from .models import Category, MenuItem, Booking


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]

    search_fields = [
        "title",
    ]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "price",
        "featured",
        "category",
    ]

    list_filter = [
        "featured",
        "category",
    ]

    search_fields = [
        "title",
        "category__title",
    ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "no_of_guests",
        "booking_date",
    ]

    list_filter = [
        "booking_date",
    ]

    search_fields = [
        "name",
    ]