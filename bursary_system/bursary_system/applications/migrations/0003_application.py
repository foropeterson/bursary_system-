# Generated by Django 5.0.3 on 2024-05-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0002_allocation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("applicant_name", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=50)),
                (
                    "amount_requested",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]