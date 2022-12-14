# Generated by Django 4.1.3 on 2022-12-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="user",
            name="currency",
            field=models.CharField(
                choices=[("won", "Won"), ("use", "Dollar")], default="won", max_length=5
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")],
                default="female",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                choices=[("kr", "Kr"), ("en", "En")], default="ko", max_length=2
            ),
        ),
    ]
