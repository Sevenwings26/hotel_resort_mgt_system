# Generated by Django 4.2.16 on 2024-11-08 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hotel", "0005_alter_room_room_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="slug",
            field=models.SlugField(blank=True, default="room", unique=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.CharField(
                choices=[
                    ("Family", "Family"),
                    ("Presidential", "Presidential"),
                    ("Single", "Single"),
                ],
                default="Family",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("customer_name", models.CharField(max_length=100)),
                ("check_in", models.DateField()),
                ("check_out", models.DateField()),
                ("booking_date", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="hotel.room",
                    ),
                ),
            ],
        ),
    ]
