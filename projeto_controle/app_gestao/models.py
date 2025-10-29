from django.db import models

# Create your models here.
class Gestao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    ativo = models.BooleanField(default=True)
    eh_terceiro = models.BooleanField()
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.cpf = self.limpa_cpf()
        super().save(*args, **kwargs)

    def clean_fields(self, exclude = ...):
        self.cpf = self.limpa_cpf()
        return super().clean_fields(exclude)    

    def cpf_formatado(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
    
    def limpa_cpf(self):
        import re
        return re.sub(r'[^0-9]', '', self.cpf)
    
    def obtem_tipo_funcionario(self):
        return "Terceiro" if self.eh_terceiro else "Próprio"