from django.contrib import admin
from .models import Agendamento

# Register your models here.

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data', 'horario', 'criado_em']
    list_filter = ['data', 'horario']
    search_fields = ['nome', 'email', 'telefone']
    date_hierarchy = 'data'
