# Generated by Django 5.0.1 on 2024-01-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
