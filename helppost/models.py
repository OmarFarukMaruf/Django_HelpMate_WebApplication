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


class HelpPost(models.Model):
    name = models.CharField(max_length=50, default=None)
    district = models.CharField(
        choices=DISTRICT_CHOISE, max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    address = models.CharField(max_length=100, default = None)
    post = models.TextField()
    post_time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=50, default=None)
    image = models.ImageField(upload_to= 'photos/post_help', default = "")
    emergency = models.BooleanField(default=False)


def __str__(self):
    return self.name
