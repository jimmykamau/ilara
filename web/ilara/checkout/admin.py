from django.contrib import admin
from ilara.checkout.models import Order, OrderItem, Payment

admin.site.register([Order, OrderItem, Payment])
