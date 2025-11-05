from django.contrib import admin
from .models import Treinamento, TreinamentoColaborador

# Register your models here.
@admin.register(Treinamento)
class TreinamentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'validade_em_meses', 'quantidade_horas_formatada')



@admin.register(TreinamentoColaborador)
class TreinamentoColaboradorAdmin(admin.ModelAdmin):
    list_display = ('treinamento', 'colaborador', 'data_treinamento', 'dias_restantes_do_treinamento', 'treinamento_esta_em_dia')
    search_fields = ('treinamento', 'colaborador')  