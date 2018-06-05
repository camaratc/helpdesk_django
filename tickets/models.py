from django.db import models
from django.utils import timezone

# Create your models here.
STATUS_CHOICE = (
    (0, "em Aberto"),
    (1, "em Andamento"),
    (2, "Finalizado")
)

class Ticket(models.Model):
    titulo = models.CharField("Título", max_length=45)
    descricao = models.TextField("Descrição", max_length=2000)
    autor = models.CharField("Autor", max_length=100)
    email = models.CharField("E-mail", max_length=45)
    departamento = models.CharField("Departamento", max_length=45)
    dataAbertura = models.DateTimeField("Data de Abertura", default = timezone.now())
    status = models.IntegerField("Status", default=0, choices=STATUS_CHOICE)
    codigo = models.CharField("Código", max_length=20)

    class Meta:
        verbose_name = u"Ticket"
        verbose_name_plural = u"Tickets"

    def __str__(self):
        return self.titulo