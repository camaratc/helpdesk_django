from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string

import random

from .models import Ticket
from .models import Comentario

from .forms import TicketForm
from .forms import BuscarTicketForm

def home(request):
    return render(request, 'tickets/home.html', {})

def detalhes_solicitacao(request, codigo):
    ticket = get_object_or_404(Ticket, codigo=codigo)
    comentarios = []

    if Comentario.objects.filter(ticket=ticket.pk).exists():
        comentarios = get_list_or_404(Comentario, ticket=ticket.pk)
    else:
        comentarios.append(Comentario(texto="Ainda não há comentários para este chamado.", data=False))

    status = ""

    if ticket.status == 0:
        status = "Aberto"
    elif ticket.status == 1:
        status = "em Andamento"
    elif ticket.status == 2:
        status = "Fechado"

    context = {
        'ticket': ticket,
        'status': status,
        'comentarios': comentarios
    }

    return render(request, 'tickets/detalhes.html', context)

def solicitar_suporte(request):
    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.dataAbertura = timezone.now()
            ticket.status = 0
            ticket.codigo = definir_codigo(ticket.dataAbertura)

            assunto = "Abertura de chamado"
            msg_basica = "Sua solicitação '" + ticket.titulo + "' foi recebida, Acompanhe pelo ID do chamado: " + ticket.codigo + "."
            remetente = "helpdesk@camaratc.mg.gov.br"
            destinatario = ticket.email

            msg_context = {
                'titulo': ticket.titulo,
                'codigo': ticket.codigo,
                'dominio': request.get_host
            }
            msg_html = render_to_string('email_template.html', msg_context)

            send_mail(
                assunto,
                msg_basica,
                remetente,
                [destinatario],
                html_message=msg_html,
                fail_silently=False
            )

            ticket.save()

            return redirect('tickets:detalhes_solicitacao', codigo=ticket.codigo)
    else:
        form = TicketForm()
        
    return render(request, 'tickets/solicitar_suporte.html', {'form': form})

def buscar_solicitacao(request):
    if request.method == "POST":
        form = BuscarTicketForm(request.POST)

        if form.is_valid():
            busca = form.cleaned_data['cod']

            return redirect('tickets:detalhes_solicitacao', codigo=busca)
    else:
        form = BuscarTicketForm()
    
    return render(request, 'tickets/buscar_solicitacao.html', {'form': form})

def erro_404(request):
    return render(request, '404.html', {})

# GERAR CÓDIGO
def dois_ultimos_digitos(num, last_digits_count=2):
    return abs(num) % (10**last_digits_count)
    
def gerar_codigo(data):
    ano = dois_ultimos_digitos(int(data.strftime("%Y")))
    prefixo = data.strftime(str(ano)+"%m%d")
    sufixo = str(random.randint(1000, 9999))
    cod = prefixo+sufixo

    return cod

def definir_codigo(data):
    cod = gerar_codigo(data)

    while Ticket.objects.filter(codigo=cod).exists():
        print("ERRO: CÓDIGO JÁ EXISTE! Gerando novo código...")
        cod += gerar_codigo(data)

        if not Ticket.objects.filter(codigo=cod).exists():
            break
        
    return cod
