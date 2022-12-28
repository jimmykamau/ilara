import tempfile
from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from ilara.backoffice.models import UserProfile
from ilara.checkout.models import Order, OrderItem
from ilara.inventory.models import Product


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user_creds = {
            "username": "jdoe",
            "email": "jdoe@example.com",
            "password": "jdoe123",
        }
        self.user = User.objects.create_user(**self.user_creds)
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            birthday=datetime.today(),
            gender=1,
            phone="+123456789",
            address="Nowhere, Middle Of.",
        )
        self.client.login(
            username=self.user_creds["username"], password=self.user_creds["password"]
        )
        temp_image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.product1 = Product.objects.create(
            name="Product 1",
            description="Product 1 description",
            price=100,
            active=True,
            stock_quantity=10,
            image=temp_image,
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            description="Product 2 description",
            price=200,
            active=True,
            stock_quantity=20,
            image=temp_image,
        )


class StoreFrontViewTestCase(BaseTest):
    def setUp(self) -> None:
        self.url = reverse("storefront")
        return super().setUp()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertTrue(response.status_code, 200)
        products = Product.objects.filter(active=True)
        self.assertQuerysetEqual(response.context["products"], products, ordered=False)
        self.assertEqual(response.context["user"], self.user)

    def test_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertTrue(response.status_code, 302)


class CartView(BaseTest):
    def setUp(self) -> None:
        self.url = reverse("cart")
        return super().setUp()

    def test_get_new_cart(self):
        order = Order.objects.filter(user=self.user)
        self.assertEqual(0, order.count())
        response = self.client.get(self.url)
        order = Order.objects.get(user=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(order, response.context["order"])

    def test_get_existing_cart(self):
        order = Order.objects.create(user=self.user, is_paid=False)
        OrderItem.objects.create(order=order, product=self.product1)
        items_queryset = OrderItem.objects.filter(order=order)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(order, response.context["order"])
        self.assertQuerysetEqual(
            response.context["items"], items_queryset, ordered=False
        )

    def test_add_item_to_cart(self):
        Order.objects.create(user=self.user, is_paid=False)
        post_data = {"productId": self.product1.pk}
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200)
        updated_order = Order.objects.get(user=self.user)
        self.assertEqual(self.product1.price, updated_order.amount)


class CartItemViewTestCase(BaseTest):
    def setUp(self) -> None:
        super().setUp()
        self.order = Order.objects.create(user=self.user, is_paid=False)

    def test_delete_cart_item(self):
        self.client.post(reverse("cart"), data=dict(productId=self.product1.pk))
        self.client.post(reverse("cart"), data=dict(productId=self.product2.pk))
        url = reverse("cart_item", args=[self.product1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        order = Order.objects.get(user=self.user)
        self.assertEqual(order.amount, self.product2.price)
