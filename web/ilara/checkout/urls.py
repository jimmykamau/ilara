from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from ilara.checkout.views import (
    CartItemView,
    CartView,
    CheckoutView,
    ReassignOrderView,
    StoreFrontView,
)

urlpatterns = [
    path("", StoreFrontView.as_view(), name="storefront"),
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/<str:item_id>/", CartItemView.as_view(), name="cart_item"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path(
        "checkout/reassign/",
        staff_member_required(ReassignOrderView.as_view()),
        name="reassign_order",
    ),
]
