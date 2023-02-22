from django.db import models
from common.models import CommonModel

# Create your models here.

class Experience(CommonModel):

    city = models.CharField(max_length=80, default="서울")
    country = models.CharField(max_length=50, default="한국")
    name = models.CharField(max_length=250,)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()

    perks = models.ManyToManyField("experiences.Perk", related_name="experiences",)

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self) -> str:
        return self.name

    def rating(experience):
        count = experience.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in experience.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)

class Perk(CommonModel):

    """"What is included on an experience"""

    name = models.CharField(max_length=100)
    details = models.CharField(
        max_length=250,
        blank=True,
        default=""
    )
    explanation = models.TextField(
        blank=True,
        default=""
    )

    def __str__(self) -> str:
        return self.name

