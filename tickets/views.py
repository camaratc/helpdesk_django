from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse

from .models import Ticket
from .forms import TicketForm

class IndexView(generic.ListView):
    template_name = 'tickets/index.html'

    def get_queryset(self):
        return 0

class DetailView(generic.DetailView):
    model = Ticket
    template_name = 'tickets/detail.html'

def solicitar(request):
    if request.method = "POST":
        form = TicketForm

        if form.is_valid:
            pass
