from django.db import models

# Create your models here.


class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking from {self.check_in} to {self.check_out} (Adults: {self.adults}, Children: {self.children})"
