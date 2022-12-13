from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    """Media Photo Model Definition"""

    file = models.ImageField()
    description = models.TextField()
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="photos",
    )

    def __str__(self) -> str:
        return "Photo File"


class Video(CommonModel):

    """Media Video Model Definition"""

    file = models.FileField()
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self) -> str:
        return "Video File"
