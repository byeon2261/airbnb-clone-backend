from django.db import models


class House(models.Model):

    """Model Definition for House"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="price",
        help_text="Positive Numbers only!",
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=False,
        help_text="당신은 애완동물을 사랑합니까?",
        verbose_name="Pets Allowed?",
    )

    def __str__(self):
        return self.name
