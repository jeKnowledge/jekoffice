from django.db import models


class Salas(models.Model):
    nome         = models.CharField(max_length = 3)

    def __str__(self):
        return "%s" % (self.nome)

class Rentals(models.Model):#acabar horas
    HORAS_CHOICES = (
    ('00:00','00:00'),   ('00:30','00:30'),   ('01:00','01:00'),   ('01:30','01:30'),
    ('02:00','02:00'),   ('02:30','02:30'),   ('03:00','03:00'),   ('03:30','03:30'),
    ('04:00','04:00'),   ('04:30','04:30'),   ('05:00','05:00'),
    )
    user_rental      = models.CharField(max_length = 30)
    sala             = models.ForeignKey(Salas, on_delete=models.CASCADE)
    dia              = models.DateField(null=True)
    data_inicio      = models.CharField(max_length = 6,choices=HORAS_CHOICES)  #seria hora
    data_final       = models.CharField(max_length = 6,choices=HORAS_CHOICES)  #seria hora
    notas            = models.TextField(null = True,blank = True)

    def __str__(self):
        return self.user_rental

    def duracao_horas(self):
        inicio   = int(self.data_inicio[:2]) * 60 + int(self.data_inicio[3:])
        final    = int(self.data_final[:2]) * 60 + int(self.data_final[3:])
        return (final - inicio)/60
    # def duracao(self):
    #     return ((self.data_final - self.data_inicio).total_seconds())/3600



    class Meta:
        ordering = ('sala',)
