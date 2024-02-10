from django.urls import path
from django.contrib.auth import views
from authentication.views import (
    Login,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    Signup
)

app_name = "authenticate"
urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password-reset/", PasswordResetView.as_view(), name="reset_password"),
    path("password-reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]