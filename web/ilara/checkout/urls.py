from django.urls import path
from ilara.checkout.views import CartItemView, CartView, StoreFrontView

urlpatterns = [
    path("", StoreFrontView.as_view(), name="storefront"),
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/<str:item_id>/", CartItemView.as_view(), name="cart_item"),
]
