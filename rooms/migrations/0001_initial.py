# Generated by Django 4.1.3 on 2022-12-07 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=140)),
                ("description", models.CharField(default="", max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("country", models.CharField(default="한국", max_length=50)),
                ("city", models.CharField(default="서울", max_length=50)),
                ("price", models.PositiveIntegerField()),
                ("rooms", models.PositiveIntegerField()),
                ("toilets", models.PositiveIntegerField()),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=250)),
                ("pet_friendly", models.BooleanField(default=False)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("entire_place", "Entire Place"),
                            ("private_room", "Private Room"),
                            ("shared_room", "Shared Room"),
                        ],
                        max_length=20,
                    ),
                ),
                ("amenities", models.ManyToManyField(to="rooms.amenity")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
