# Generated by Django 5.1.5 on 2025-02-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("travels", "0010_remove_destination_deatils_disliked_by_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IPAddress",
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
                ("ip_address", models.GenericIPAddressField(unique=True)),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
