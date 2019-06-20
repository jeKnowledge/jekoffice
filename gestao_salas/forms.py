from django import forms
from .models import Rentals,Salas


class RentalForm(forms.Form):
    HORAS_CHOICES = (
    ('00:00','00:00'),   ('00:30','00:30'),   ('01:00','01:00'),   ('01:30','01:30'),
    ('02:00','02:00'),   ('02:30','02:30'),   ('03:00','03:00'),   ('03:30','03:30'),
    ('04:00','04:00'),   ('04:30','04:30'),   ('05:00','05:00'),
    )

    dia                 = forms.DateField()
    data_inicio         = forms.ChoiceField(choices= HORAS_CHOICES, label = 'Hora Início')
    data_final          = forms.ChoiceField(choices= HORAS_CHOICES, label = 'Hora Final')
    notas               = forms.CharField(required = False,widget=forms.Textarea)
