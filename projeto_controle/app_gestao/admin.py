from django.contrib import admin
from .models import Gestao

# Register your models here.
@admin.register(Gestao)
class GestaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf_formatado', 'cargo', 'eh_terceiro', 'ativo')
    search_fields = ('nome', 'cpf', 'cargo')
    list_filter = ('eh_terceiro', 'ativo')