from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Kr")
        EN = ("en", "En")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Won")
        USD = ("usd", "Dollar")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
    )
    avatar = models.URLField(
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default="female",
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default="ko",
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        default="won",
    )
