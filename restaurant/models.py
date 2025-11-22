from django.db import models
from django.contrib.auth.models import User

# ----------------------------
# Menu Model
# ----------------------------
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# ----------------------------
# Booking Model
# ----------------------------
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"Booking by {self.user.username} on {self.date} at {self.time}"
