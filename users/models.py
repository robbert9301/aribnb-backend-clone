from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Recreating evertying about user
class User(AbstractUser) :

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male") #(데이터베이스, 관리자 패널)
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    avatar = models.URLField(blank=True) #Pillow 필요 blank=True 이미지를 안넣어도 되게 만듬

    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices) #making choices

    language = models.CharField(max_length=2, choices=LanguageChoices.choices)

    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)


