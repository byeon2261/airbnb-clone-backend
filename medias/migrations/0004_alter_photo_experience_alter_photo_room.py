# Generated by Django 4.1.3 on 2022-12-29 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "experiences",
            "0004_alter_experience_category_alter_experience_host_and_more",
        ),
        ("rooms", "0006_alter_room_amenities_alter_room_category_and_more"),
        ("medias", "0003_alter_photo_file_alter_video_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="experience",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
    ]
