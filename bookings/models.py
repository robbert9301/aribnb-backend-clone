from django.db import models
from common.models import CommonModel

class Booking(CommonModel):

    """ Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):

        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices
    )

    #Booking 입장에서 생각해야함
    # user의 경우에는 많은 부킹을 가질수 있지만 부킹의 경우에는 1개의 유저만 갖고있어야하기 때문에
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )
    
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookings",
    )

    check_in = models.DateField(null=True, blank=True,)
    check_out = models.DateField(null=True, blank=True,)

    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()}  booking for : {self.user}"