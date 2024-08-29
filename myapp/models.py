from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TYPE_STAFF_CHOICES = (
        ('admin', 'Admin'),
        ('seller', 'Seller'),
    )
    type_staff = models.CharField(max_length=10, choices=TYPE_STAFF_CHOICES, default='seller')

    def __str__(self):
        return self.username
