from django.db import models

# Create your models here.
class Processos(models.Model):
    #choices
    DEPARTAMENTOS_CHOICES = (
    ('INO','INO'),
    ('TEC','TEC'),
    ('INT','INT'),
    )
    ESTADOS_CHOICES = (
    ('BASELINE','BASELINE'),
    ('DRAFT','DRAFT')
    )
    VALIDACAO_CHOICES = (
    ('SIM','SIM'),
    ('NAO','NAO'),
    )


    #____
    nome            = models.CharField('Nome',max_length = 20)
    departamento    = models.CharField('Departamento',max_length = 3, choices = DEPARTAMENTOS_CHOICES)
    data_criacao    = models.DateField("Data criação", auto_now=True)
    estado          = models.CharField("Estado", max_length = 8, choices = ESTADOS_CHOICES)
    validacao       = models.BooleanField("Validaçao")
    cond_entrada    = models.TextField("Condicoes entrada")
    cond_saida      = models.TextField("Condicoes saída")
    inputs          = models.TextField("Inputs")
    outputs         = models.TextField("Outputs")
    metricas        = models.TextField("Métricas")
    autor           = models.CharField("Autor",max_length = 20)
    documento       = models.FileField(upload_to='processos/', null = True, blank = True)
