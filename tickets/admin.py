from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    search_fields = ('autor', 'departamento', 'titulo', 'status', 'dataAbertura', 'codigo')
    list_filter = ('status', 'autor', ('dataAbertura', DateTimeRangeFilter), 'departamento')
    list_display = ('titulo', 'autor', 'dataAbertura', 'codigo')
    ordering = ['-dataAbertura']
    list_per_page = 10

admin.site.register(Ticket, TicketAdmin)