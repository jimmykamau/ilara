from django.urls import path
from ilara.backoffice.views import (
    AuthView,
    CreateAnonymousUserView,
    GetUserView,
    LogoutView,
)
from ilara.checkout.views import StoreFrontView

urlpatterns = [
    path("", StoreFrontView.as_view()),
    path("user/", GetUserView.as_view(), name="get_user"),
    path("login/", AuthView.as_view(), name="login"),
    path("signup/anon/", CreateAnonymousUserView.as_view(), name="create_anon_user"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
