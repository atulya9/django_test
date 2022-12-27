from django.db import models

# Create your models here.
class Order(models.Model):
    status = models.CharField(max_length=255)
    user_ID = models.IntegerField()
    address = models.TextField()
