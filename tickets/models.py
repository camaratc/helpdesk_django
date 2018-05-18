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
        ordering = ['titulo', 'descricao']

    def __unicode__(self):
        return u"%s - %s" % (self.titulo, self.autor)

    '''
    class Meta:
        verbose_name = u"Processo de Matrícula - Série"
        verbose_name_plural = u"Processos de Matrículas - Séries"
        unique_together = ('ProcessoMatricula', 'Serie')
        ordering = ['ProcessoMatricula', 'Serie']

    def __unicode__(self):
        return u"%s - %s" % (self.ProcessoMatricula.AnoLetivo, self.Serie.Descricao)

    '''