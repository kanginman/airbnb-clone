from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = ((GENDER_MALE), (GENDER_FEMALE), (GENDER_OTHER))
    avatar = models.ImageField(null=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, null=True)
    bio = models.TextField(default="")
