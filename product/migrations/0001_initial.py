# Generated by Django 5.1.2 on 2024-10-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("img", models.ImageField(upload_to="product_images/")),
                ("productName", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("color", models.CharField(max_length=100)),
                ("badge", models.BooleanField(default=False)),
                ("des", models.TextField()),
                ("brand", models.CharField(max_length=100)),
            ],
        ),
    ]
