from django.db import models
from common.models import CommonModel

class Photo(CommonModel):

    file = models.URLField()
    description = models.CharField(max_length=140,)

    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    def __str__(self) -> str:
        return "Photo File"

class Video(CommonModel):

    file = models.URLField()
    # one to one 딱 1개의 1동영상만 가질수있음 - 하지만 흔치 않음
    # ex payment
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )
    def __str__(self) -> str:
        return "Video File"