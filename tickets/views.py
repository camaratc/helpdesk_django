from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Ticket
from .forms import TicketForm
from .forms import BuscarTicketForm

def home(request):
    return render(request, 'tickets/home.html', {})

def detalhes_solicitacao(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    status = ""

    if ticket.status == 0:
        status = "Aberto"
    elif ticket.status == 1:
        status = "em Andamento"
    elif ticket.status == 2:
        status = "Fechado"

    context = {
        'ticket': ticket,
        'status': status
    }

    return render(request, 'tickets/detalhes.html', context)

def solicitar_suporte(request):
    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.dataAbertura = timezone.now()
            ticket.status = 0
            ticket.save()

            return redirect('tickets:detalhes_solicitacao', pk=ticket.pk)
    else:
        form = TicketForm()
        
    return render(request, 'tickets/solicitar_suporte.html', {'form': form})

def buscar_solicitacao(request):
    if request.method == "POST":
        form = BuscarTicketForm(request.POST)

        if form.is_valid():
            busca = form.cleaned_data['cod']

            return redirect('tickets:detalhes_solicitacao', pk=busca)
    else:
        form = BuscarTicketForm()
    
    return render(request, 'tickets/buscar_solicitacao.html', {'form': form})

def erro_404(request):
    return render(request, '404.html', {})
