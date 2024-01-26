from django.shortcuts import render
from django.views import View

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')


class SignInView(View):
    def get(self, request):
        return render(request, 'signin.html')