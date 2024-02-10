from django.contrib.auth import views
from django.views import View
from django.urls import reverse_lazy
from authentication.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

from authentication.models import TicketingUser

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        student_email = request.POST.get("email")
        password = request.POST.get("password")
        registration_number = request.POST.get("regno")
        user = TicketingUser.objects.create(username=registration_number, email=student_email, password=password, registration_number=registration_number, user_type="student")
        user.save()
        login(request, user)
        return redirect("dashboard:index")
    
class Login(View):
    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = TicketingUser.objects.get(username=username, password=password)
        login(request, user)
        return redirect("dashboard:index")

class LoginView(views.LoginView):
    template_name = "login.html"
    # authentication_form = LoginForm

class PasswordResetView(views.PasswordResetView):
    template_name = "password_reset.html"
    success_url = reverse_lazy("authenticate:password_reset_done")


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "password_reset_done.html"

class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"

class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "password_reset_complete.html"
