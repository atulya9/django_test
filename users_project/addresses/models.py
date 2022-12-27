from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    address_line_3 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.address_line_1}, {self.address_line_2}, {self.address_line_3}, {self.city}, {self.state}, {self.country}-{self.zip_code}'