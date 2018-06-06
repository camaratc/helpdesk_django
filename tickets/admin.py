from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django_admin_relation_links import AdminChangeLinksMixin

from .models import Ticket
from .models import Comentario

# Register your models here.

class TicketAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    search_fields = ('autor', 'departamento', 'titulo', 'status', 'dataAbertura', 'codigo')
    list_filter = ('status', 'autor', ('dataAbertura', DateTimeRangeFilter), 'departamento')
    list_display = ('titulo', 'autor', 'dataAbertura', 'codigo')
    ordering = ['-dataAbertura']
    list_per_page = 10
    changelist_links = ['comentario']

class ComentarioAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ['texto']
    change_links = ['ticket']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comentario, ComentarioAdmin)