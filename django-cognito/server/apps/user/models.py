from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    user_type_choices = ((0, 'Default'), (1, 'Admin'), (2, 'Develop'), (3, 'Trial'), (4, 'Corporate'),)

    nick_name = models.CharField(max_length=50, null=True, default=None, verbose_name="Nick name")
    email = models.CharField(max_length=254, unique=True, null=False, verbose_name="Email")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="Birthday")
    is_staff = models.BooleanField(default=True, verbose_name="Is stuff")
    is_active = models.BooleanField(default=True, verbose_name="IS activate")
    user_type = models.IntegerField(choices=user_type_choices, default=0, verbose_name="User type")
    company = models.CharField(max_length=254, null=True, blank=True, default=None, verbose_name="Company")
    title = models.CharField(max_length=254, null=True, blank=True, default=None, verbose_name="Title")
    email_flag = models.IntegerField(default=0, verbose_name="Email validation")
    trial_date = models.DateField(null=True, blank=True, verbose_name='Trial date')
    trial_model = models.CharField(
        max_length=254, null=True, blank=True, default=None, verbose_name="Trial model",
        help_text="Value must be one or multiply item(s) in the list ['CONCEPT_SEARCH', 'API_BAIDU', 'DATASET_CHINA_ISSUER'] and separated by semi-colon(;)"
    )
    stripe_id = models.CharField(max_length=254, null=True, unique=True, verbose_name="Stripe ID")
    unique_id = models.CharField(max_length=254, null=True, unique=True, verbose_name="Unique ID")
    currency = models.CharField(max_length=20, null=True, unique=False, verbose_name="Currency")
    pic_path = models.CharField(max_length=254, null=True, verbose_name="Pic path")
    phone = models.CharField(max_length=50, null=True, verbose_name="Phone number")

    class Meta:
        verbose_name = "User Management"
        verbose_name_plural = verbose_name
