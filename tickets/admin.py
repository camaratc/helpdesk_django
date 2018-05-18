from django.contrib import admin
from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    search_fields = ('autor', 'departamento', 'titulo', 'status', 'dataAbertura')
    list_filter = ('autor', 'departamento', 'status', 'dataAbertura')
    list_display = ('titulo', 'autor', 'dataAbertura')

admin.site.register(Ticket, TicketAdmin)