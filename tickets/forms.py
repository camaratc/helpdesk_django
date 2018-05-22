from django import forms

STATUS_CHOICE = (
    (0, "Aberto"),
    (1, "Andamento"),
    (2, "Finalizado")
)

class TicketForm(forms.Form):
    titulo = forms.CharField("Título", max_length=45)
    descricao = forms.TextField("Descrição", max_length=2000)
    autor = forms.CharField("Autor", max_length=100)
    email = forms.CharField("E-mail", max_length=45)
    departamento = forms.CharField("Departamento", max_length=45)
    dataAbertura = forms.DateTimeField("Data de Abertura")
    status = forms.IntegerField("Status", choices=STATUS_CHOICE)