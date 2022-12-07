from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room or Experience Category model Definition"""

    class CategoryKindChoice(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Ecperiences")

    name = models.CharField(
        max_length=50,
    )
    kind = models.CharField(
        max_length=30,
        choices=CategoryKindChoice.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
