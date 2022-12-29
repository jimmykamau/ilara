from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from ilara.inventory.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"Order #{self.pk} - User: {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    comments = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Order #{self.order.pk} - {self.product.name}"

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")


class Payment(models.Model):
    FAILED = "fe2707etr5s4wq"
    SUCCESS = "aei7p7yrx4ae34"
    PENDING = "bdi6p2yy76etrs"
    USED = "cr5i3pgy9867e1"
    LESS = "dtfi4p7yty45wq"
    MORE = "eq3i7p5yt7645e"
    CASH = "cash"
    PAYMENT_STATUS_CHOICES = [
        (FAILED, _("Failed")),
        (SUCCESS, _("Success")),
        (PENDING, _("Pending")),
        (USED, _("Used")),
        (LESS, _("Less")),
        (MORE, _("More")),
        (CASH, _("Cash")),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_code = models.CharField(max_length=150, null=True, blank=True)
    payment_name = models.CharField(max_length=150, null=True, blank=True)
    payer_phone = models.CharField(max_length=150, null=True, blank=True)
    card_mask = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(
        max_length=150, choices=PAYMENT_STATUS_CHOICES, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order #{self.order.pk} - {self.amount_paid}"
