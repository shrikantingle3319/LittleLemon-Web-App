from rest_framework import serializers

from .models import Category, MenuItem, Booking


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
        ]


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.title",
        read_only=True
    )

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "title",
            "price",
            "featured",
            "category",
            "category_name",
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "name",
            "no_of_guests",
            "booking_date",
        ]

    def validate_no_of_guests(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "There must be at least one guest."
            )

        if value > 20:
            raise serializers.ValidationError(
                "A booking cannot exceed 20 guests."
            )

        return value