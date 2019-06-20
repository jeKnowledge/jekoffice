from django.shortcuts import render
from .models import Salas,Rentals
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import RentalForm


def salas_home_view(request,*args,**kargs):
    hora_inicial        = request.GET.get('inicio',None)
    hora_fim            = request.GET.get('fim',None)
    salas               = Salas.objects.all()
    salas_ocupadas      = []
    get_flag            = 1;

    if (hora_inicial and hora_fim):
        query_set       = Rentals.objects.filter((Q(data_inicio__gte=hora_inicial) & Q(data_inicio__lt=hora_fim))|(Q(data_final__gt=hora_inicial) & Q(data_final__lte=hora_fim)))
        get_flag        = 0;
        for instance in query_set:
            salas_ocupadas.append(instance.sala.nome)
    return render(request,"salas_home_page.html",{'salas_query':salas,
                                                  'salas_ocupadas_lista':salas_ocupadas,
                                                  'get_flag': get_flag})


def salas_rental_view(request,sala_slug):  #VALIDACOES FALTA
    sala                = get_object_or_404(Salas, nome=sala_slug.upper())
    my_form             = RentalForm()
    dados_form = {}
    if request.method == 'POST':
        my_form = RentalForm(request.POST)
        if my_form.is_valid():
            dados_form = my_form.cleaned_data
            dados_form['sala'] = sala
            dados_form['user_rental'] = request.user.username

#            date=dados['date']
#            time = dados['time']
#            datetime = date + time
#            novo = Rentals(date=datetime)

            Rentals.objects.create(**dados_form)
        else:
            print(my_form.errors)
    return render(request,"rentals.html",{'form':my_form,
                                          'sala':sala})
