from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, null=True, default=None, verbose_name="NICK NAME")
    email = models.CharField(max_length=254, unique=True, null=False, verbose_name="EMAIL")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="BIRTHDAY")
    phone = models.CharField(max_length=50, null=True, verbose_name="PHONE")

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'User Profile'
