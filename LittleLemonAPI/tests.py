from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, MenuItem, Booking


class CategoryModelTest(APITestCase):

    def test_category_creation(self):
        category = Category.objects.create(
            title="Desserts"
        )

        self.assertEqual(
            category.title,
            "Desserts"
        )


class MenuItemModelTest(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title="Main Course"
        )

    def test_menu_item_creation(self):
        item = MenuItem.objects.create(
            title="Grilled Fish",
            price=18.50,
            featured=True,
            category=self.category,
        )

        self.assertEqual(
            item.title,
            "Grilled Fish"
        )

        self.assertEqual(
            float(item.price),
            18.50
        )


class BookingModelTest(APITestCase):

    def test_booking_creation(self):
        booking = Booking.objects.create(
            name="John",
            no_of_guests=4,
            booking_date=timezone.now(),
        )

        self.assertEqual(
            booking.name,
            "John"
        )

        self.assertEqual(
            booking.no_of_guests,
            4
        )


class MenuItemAPITest(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title="Main Course"
        )

        self.menu_item = MenuItem.objects.create(
            title="Pasta",
            price=12.99,
            featured=True,
            category=self.category,
        )

        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

    def test_menu_list_public(self):
        url = reverse("menu-item-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_menu_create_requires_authentication(self):
        url = reverse("menu-item-list")

        data = {
            "title": "Pizza",
            "price": "15.00",
            "featured": False,
            "category": self.category.id,
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_authenticated_user_can_create_menu_item(self):
        self.client.force_authenticate(
            user=self.user
        )

        url = reverse("menu-item-list")

        data = {
            "title": "Pizza",
            "price": "15.00",
            "featured": False,
            "category": self.category.id,
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            MenuItem.objects.count(),
            2
        )


class BookingAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="bookinguser",
            password="TestPassword123!"
        )

    def test_booking_requires_authentication(self):
        url = reverse("booking-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(
            user=self.user
        )

        url = reverse("booking-list")

        data = {
            "name": "Alice",
            "no_of_guests": 3,
            "booking_date": (
                timezone.now() + timedelta(days=1)
            ).isoformat(),
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Booking.objects.count(),
            1
        )