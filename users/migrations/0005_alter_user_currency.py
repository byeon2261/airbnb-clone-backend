# Generated by Django 4.1.3 on 2023-02-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="currency",
            field=models.CharField(
                choices=[("won", "Won"), ("usd", "Dollar")], default="won", max_length=5
            ),
        ),
    ]
