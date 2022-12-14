# Generated by Django 4.1.3 on 2022-12-13 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "experiences",
            "0004_alter_experience_category_alter_experience_host_and_more",
        ),
        ("rooms", "0005_room_category"),
        ("medias", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="experience",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="experience",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="experiences.experience",
            ),
        ),
    ]
