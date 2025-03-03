# Generated by Django 5.1.5 on 2025-01-29 18:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("travels", "0009_destination_deatils_disliked_by_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="destination_deatils",
            name="disliked_by",
        ),
        migrations.RemoveField(
            model_name="destination_deatils",
            name="liked_by",
        ),
        migrations.AddField(
            model_name="destination",
            name="disliked_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="disliked_destinations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="destination",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="liked_destinations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
