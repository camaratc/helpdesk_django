from django.db import models

# Create your models here.
class Ticket(models.Model):
    titulo = models.CharField("Título", max_length=45)
    descricao = models.TextField("Descrição", max_length=2000)
    autor = models.CharField("Autor", max_length=100)
    email = models.CharField("E-mail", max_length=45)
    departamento = models.CharField("Departamento", max_length=45)
    dataAbertura = models.DateTimeField("Data de Abertura")
    status = models.IntegerField()

    class Meta:
        verbose_name = u"Ticket"
        verbose_name_plural = u"Tickets"

    def __unicode__(self):
        return u"%s - %s" % (self.titulo, self.autor)
