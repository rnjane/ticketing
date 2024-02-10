from django.shortcuts import render, redirect
from django.views import View

from dashboard.forms import TicketForm
from dashboard.models import Ticket

class Index(View):
    def get(self, request):
        form = TicketForm()
        tickets = Ticket.objects.filter(created_by=request.user)
        context = {
            "form": form,
            "tickets": tickets
        }
        return render(request, "index.html", context)
    
    def post(self, request):
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket.objects.create(summary=form.cleaned_data["summary"], description=form.cleaned_data["description"], created_by=request.user)
            ticket.save()
            return redirect("dashboard:index")
        tickets = Ticket.objects.filter(created_by=request.user)
        context = {
            "form": form,
            "tickets": tickets
        }
        return render(request, "index.html", context=context)
