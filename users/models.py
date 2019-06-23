from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    CARGOS_CHOICES = (("Software developer","Software developer"),
                    ("Designer","Designer"),
                    ("Film maker","Film maker"),
                    ("Innovation consultant","Innovation consultant"),
                    ("HR manager","HR manager"),
                    ("CFO","CFO"),
                    ("International Manager","International Manager"),
                    ("Project Manager","Project Manager"),
                    ("CEO","CEO"),
                    ("CIO","CIO"),
                    ("COO","COO"),
                    ("CTO","CTO")
                    )

    MEMBRO_CHOICES = (("Trainee","Trainee"),
                    ("Junior","Junior"),
                    ("Senior","Senior"),
                    ("Alumnus","Alumnus"),
                    ("Chief","Chief")
                    )

    DEPARTAMENTOS_CHOICES = (
                    ('INO','INO'),
                    ('TEC','TEC'),
                    ('INT','INT'),
                    )

    departamento    = models.CharField(choices = DEPARTAMENTOS_CHOICES, max_length = 3,null = True, blank = True)
    tipo_membro     = models.CharField(choices = MEMBRO_CHOICES, max_length= 5,null=True,blank = True)
    cargo           = models.CharField(choices = CARGOS_CHOICES, max_length = 20,null = True, blank = True)
    curso           = models.CharField(max_length = 20,null = True, blank = True)
    telemovel       = PhoneNumberField(null=True, blank=True, unique=True, region='PT')
    cc_num          = models.IntegerField(null=True,blank=True)
    mac_adress      = models.CharField( max_length = 5,null = True, blank = True)
    projetos        = models.ManyToManyField('interno.Projetos',related_name="projetos",blank=True, null=True)
    imagem          = models.FileField(upload_to='users/%Y/%m/%d/', null = True, blank = True)
    #permissoes
    is_super   = models.BooleanField(default = False)
    def __str__(self):
        return "%s - %s" %(self.username,self.departamento)
