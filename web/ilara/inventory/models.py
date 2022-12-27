from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="uploads/products/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Inventory Item")
        verbose_name_plural = _("Inventory Items")

    @property
    def in_stock(self):
        return self.stock_quantity > 0

    @property
    def is_active(self):
        return self.active == True
