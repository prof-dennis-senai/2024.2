from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Treinamento(models.Model):
    TRES_MESES = 3
    SEIS_MESES = 6
    UM_ANO = 12
    UM_ANO_E_MEIO = 18
    DOIS_ANOS = 24
    TRES_ANOS = 36

    OPCOES_VALIDADE = (
        (TRES_MESES, '3 meses'),
        (SEIS_MESES, '6 meses'),
        (UM_ANO, '12 meses'),
        (UM_ANO_E_MEIO, '18 meses'),
        (DOIS_ANOS, '24 meses'),
        (TRES_ANOS, '36 meses'),
    )

    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=11)
    validade_em_meses = models.PositiveIntegerField(default=SEIS_MESES, choices=OPCOES_VALIDADE)
    quantidade_horas = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

    def validade_formatada(self):
        return f'{self.validade_em_meses} meses'
    
    def quantidade_horas_formatada(self):
        return f'{self.quantidade_horas} horas'
    
class TreinamentoColaborador(models.Model):
    treinamento = models.ForeignKey(Treinamento, on_delete=models.PROTECT)
    colaborador = models.ForeignKey('app_gestao.Gestao', on_delete=models.PROTECT)
    data_treinamento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.colaborador.nome} - {self.treinamento.titulo}'
    
    def dias_restantes_do_treinamento(self):
        return (self.treinamento.validade_em_meses * 30) - (datetime.now().date() - self.data_treinamento).days
    
    def treinamento_esta_em_dia(self):
        hoje = datetime.now().date()
        return hoje < self.data_treinamento + timedelta(days=self.treinamento.validade_em_meses * 30)