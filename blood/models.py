from django.db import models
from accounts.models import CustomUser

# Create your models here.

DISTRICT_CHOISE = [
    ("1", "DHAKA"),
    ("2", "CHITTAGONG"),
    ("3", "KHULNA"),
    ("4", "RAJSHAHI"),
    ("5", "BARISHAL"),
    ("6", "DINAJPUR"),
    ("7", "RANGPUR")
]

BLOOD_GROUP = [
    ("1", "A+"),
    ("2", "A-"),
    ("3", "B+"),
    ("4", "B-"),
    ("5", "AB+"),
    ("6", "AB-"),
    ("7", "O+"),
    ("8", "O-")
]


class BloodModel(models.Model):
    name = models.CharField(max_length=50, default=None)
    district = models.CharField(
        choices=DISTRICT_CHOISE, max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    area = models.CharField(max_length=100, default = None)
    blood_group = models.CharField(BLOOD_GROUP , max_length=50)
    post_time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=50, default=None)
    comment = models.TextField(default = None)


def __str__(self):
    return self.name