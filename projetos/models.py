from django.db import models
from users.models import CustomUser


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
