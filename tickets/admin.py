from django.contrib import admin
from django.utils import timezone
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
    def get_form(self, request, obj=None, **kwargs):
        form = super(ComentarioAdmin, self).get_form(request, obj, **kwargs)
        print(form.base_fields['ticket'].initial)
        form.base_fields['data'].initial = timezone.now()
        return form

    list_display = ['texto']
    list_per_page = 10
    #change_links = ['ticket']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comentario, ComentarioAdmin)