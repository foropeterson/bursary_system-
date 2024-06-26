# Generated by Django 5.0.3 on 2024-05-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0003_application"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Application",
        ),
        migrations.RemoveField(
            model_name="allocation",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="bursaryapplication",
            name="submitted_at",
        ),
        migrations.RemoveField(
            model_name="bursaryapplication",
            name="user",
        ),
        migrations.AddField(
            model_name="bursaryapplication",
            name="institution",
            field=models.CharField(default="Unknown Institution", max_length=100),
        ),
        migrations.AlterField(
            model_name="bursaryapplication",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="bursaryapplication",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
