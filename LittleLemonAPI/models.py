from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    featured = models.BooleanField(default=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="menu_items"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255)

    no_of_guests = models.PositiveIntegerField()

    booking_date = models.DateTimeField()

    class Meta:
        ordering = ["booking_date"]

    def __str__(self):
        return f"{self.name} - {self.booking_date}"