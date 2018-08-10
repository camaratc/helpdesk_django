from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):    
    class Meta:
        model = Ticket
        fields = ('titulo', 'descricao', 'autor', 'email', 'host', 'departamento')
    
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        for item in self.fields:
            if item == 'descricao':
                self.fields[item].widget = forms.Textarea(attrs={'class': 'form-control input-descricao'})
            elif item == 'email':
                self.fields[item].widget = forms.EmailInput(attrs={'class': 'form-control'})
            else:
                self.fields[item].widget = forms.TextInput(attrs={'class': 'form-control'})

class BuscarTicketForm(forms.Form):
    cod = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control cod'}))
