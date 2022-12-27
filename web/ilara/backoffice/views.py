import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView, View
from ilara.backoffice.models import UserProfile

logger = logging.getLogger(__name__)


class GetUserView(LoginRequiredMixin, View):
    def get(self, request):
        profile = UserProfile.objects.filter(user=request.user)
        data = {"user": list(profile.values())}
        return JsonResponse(data)


class AuthView(TemplateView):
    def get(self, request):
        return render(request, "backoffice/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "success"})
        else:
            return JsonResponse({"message": "error"}, status=403)


class CreateAnonymousUserView(TemplateView):
    def post(self, request):
        logger.info("Creating anonymous user")
        username = get_random_string(length=5)
        user = User(username=username)
        user.save()
        authenticate(user=user)
        login(request, user=user)
        return JsonResponse({"message": "success"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
