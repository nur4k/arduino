# Generated by Django 4.2.7 on 2024-01-25 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
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
                (
                    "fio",
                    models.CharField(
                        blank=True, max_length=155, null=True, verbose_name="ФИО"
                    ),
                ),
                (
                    "car_number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Номер машины",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GIS",
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
                ("transmitter_id", models.IntegerField(verbose_name="ID передатчика")),
                ("latitude", models.FloatField(null=True, verbose_name="Широта")),
                ("longitude", models.FloatField(null=True, verbose_name="Долгота")),
                ("direction", models.FloatField(null=True, verbose_name="Направле")),
                ("speed", models.FloatField(null=True, verbose_name="Скорость")),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время"
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.driver",
                    ),
                ),
            ],
        ),
    ]
