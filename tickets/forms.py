from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):    
    class Meta:
        model = Ticket
        fields = ('titulo', 'descricao', 'autor', 'email', 'departamento')

class BuscarTicketForm(forms.Form):
    cod = forms.IntegerField()