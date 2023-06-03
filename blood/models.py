from django.db import models
from accounts.models import CustomUser

# Create your models here.

DISTRICT_CHOISE = [
    ("Dhaka", "DHAKA"),
    ("Chittagong", "CHITTAGONG"),
    ("Khulna", "KHULNA"),
    ("Rajshahi", "RAJSHAHI"),
    ("Barishal", "BARISHAL"),
    ("Dinajpur", "DINAJPUR"),
    ("Rangpur", "RANGPUR")
]

BLOOD_GROUP = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-")
]


class BloodModel(models.Model):
    name = models.CharField(max_length=50, default=None)
    district = models.CharField(
        choices=DISTRICT_CHOISE, max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    area = models.CharField(max_length=100, default=None)
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=50)
    post_time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=50, default=None)
    comment = models.TextField(blank=True)


def __str__(self):
    return self.name
