from django.db import models
from users.models import CustomUser
import datetime


class Projetos(models.Model):
    #choices

    ESTADOS_CHOICES = (
    ('Definition','Definition'),
    ('Initiation','Initiation'),
    ('Execution','Execution'),
    ('Monitoring & Control','Monitoring & Control'),
    ('Closure','Closure'),
    )

    OBJETIVO_CHOICES = (
    ('INTERNO','INTERNO'),
    ('EXTERNO','EXTERNO'),
    )


    #____
    nome            = models.CharField('Nome',max_length = 30)
    descrição       = models.TextField('Descrição')
    gestores        = models.ManyToManyField(CustomUser,related_name="gestores")
    colaboradores   = models.ManyToManyField(CustomUser,related_name="colaboradores")
    data_inicio     = models.DateField("Data Criação", auto_now=True)
    estado          = models.CharField("Estado", max_length = 15, choices = ESTADOS_CHOICES)
    data_fim        = models.DateField("Data Fim", auto_now=False,null=True,blank=True)
    objectivo       = models.CharField("Objectivo", max_length = 8, choices = ESTADOS_CHOICES)
# Projectos
# Nome
# descrição
# Gestores de projecto
# Colaboradores
# Data início
# Estado
# Data conclusão
# interno/externo
# Orçamento final com o cliente (apenas preenchido quando ambas as partes concordarem)
# Balanço financeiro(restrito a direcção, tesoureiro e membros gestores)
# jeKbills


class Relatorios_formacoes(models.Model):
    pass

class Relatorios_recrutamento(models.Model):
    SEMESTRE_ESCOLHA = (("1º Semestre","1º Semestre"), ("2º Semestre","2º Semestre"))
    ano = models.IntegerField(default = datetime.date.today().year)
    semestre = models.CharField(max_length = 11, choices=SEMESTRE_ESCOLHA)
    responsavel = models.ForeignKey(CustomUser,related_name="responsavel", on_delete=models.CASCADE,blank=True,null=True)
    n_vagas_tec = models.IntegerField(default=0)
    n_vagas_ino = models.IntegerField(default=0)
    n_vagas_int = models.IntegerField(default=0)
    n_candidatos = models.IntegerField(default=0)
    n_grupos = models.IntegerField(default=0)
    n_min_grupo = models.IntegerField(default=0)
    n_max_grupo = models.IntegerField(default=0)
    n_individual = models.IntegerField(default=0)
    n_estagio = models.IntegerField(default=0)
    n_admitidos = models.IntegerField(default=0)
    documento = models.FileField(upload_to='relatorios/', null = True, blank = True)
    def __str__(self):
        return "Recrutamento %d - %s" %(self.ano,self.semestre)
