import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from ilara.checkout.models import Order, OrderItem
from ilara.inventory.models import Product

logger = logging.getLogger(__name__)


class StoreFrontView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        products = Product.objects.filter(active=True)
        context = {"products": products, "user": request.user}
        return render(request, "checkout/storefront.html", context)


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)
        items = OrderItem.objects.filter(order=order)
        context = {"order": order, "items": items}
        return render(request, "checkout/cart.html", context)

    def post(self, request):
        try:
            order, created = Order.objects.get_or_create(
                user=request.user, is_paid=False
            )
            product = Product.objects.get(pk=request.POST.get("productId"))
            order_item, created = OrderItem.objects.get_or_create(
                order=order, product=product
            )
            if not created:
                order_item.quantity += 1
                order_item.save()
            order.amount += product.price
            order.save()
            return JsonResponse({"message": "success"})
        except Exception as e:
            return JsonResponse({"message": "error", "exception": str(e)})


class CartItemView(LoginRequiredMixin, View):
    def delete(self, request, item_id):
        try:
            order = Order.objects.get(user=request.user, is_paid=False)
            order_item = OrderItem.objects.get(pk=item_id, order=order)
            total_cost = order_item.product.price * order_item.quantity
            order_item.delete()
            order.amount -= total_cost
            order.save()
            return JsonResponse({"message": "success"})
        except Exception as e:
            return JsonResponse(
                data={"message": "error", "exception": str(e)}, status=404
            )
