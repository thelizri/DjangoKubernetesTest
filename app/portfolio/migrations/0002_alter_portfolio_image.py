# Generated by Django 5.0.1 on 2024-03-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
