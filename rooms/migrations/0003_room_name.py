# Generated by Django 4.1.3 on 2022-12-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_alter_amenity_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="name",
            field=models.CharField(default="", max_length=180),
        ),
    ]
