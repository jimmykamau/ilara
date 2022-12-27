# Generated by Django 4.1.4 on 2022-12-21 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0003_product_image"),
        ("backoffice", "0003_alter_userprofile_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("is_paid", models.BooleanField(default=False)),
                ("description", models.TextField(blank=True, null=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backoffice.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "transaction_code",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "payment_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "payer_phone",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("card_mask", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("fe2707etr5s4wq", "Failed"),
                            ("aei7p7yrx4ae34", "Success"),
                            ("bdi6p2yy76etrs", "Pending"),
                            ("cr5i3pgy9867e1", "Used"),
                            ("dtfi4p7yty45wq", "Less"),
                            ("eq3i7p5yt7645e", "More"),
                            ("cash", "Cash"),
                        ],
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="checkout.order"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="checkout.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.product",
                    ),
                ),
            ],
        ),
    ]
