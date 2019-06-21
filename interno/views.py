from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.static import serve
import os
from django.conf import settings
import docx
from .forms import RecrutamentoForm
from .models import Relatorios_recrutamento
from users.models import CustomUser


def relatorio_novo_view(request):
    my_form = RecrutamentoForm()

    doc = docx.Document()
    try:
        if request.method == 'POST':
            my_form = RecrutamentoForm(request.POST)
            if my_form.is_valid():
                dados_form = my_form.cleaned_data
                responsavel = dados_form['responsavel']
                user = CustomUser.objects.get(username = responsavel)
                dados_form['responsavel'] = user
                relatorio = Relatorios_recrutamento.objects.create(**dados_form)
                for instance in dados_form:
                    doc.add_paragraph(str(dados_form[instance]))
                doc.save(os.getcwd() + '/media/relatorios/' + 'Recrutamento' + str(relatorio.ano) + '-'+relatorio.semestre[0] + '.docx')
                print()
                relatorio.documento.name = '/relatorios/' + 'Recrutamento' + str(relatorio.ano) +'-'+ relatorio.semestre[0] + '.docx'
                relatorio.save()
    except:
        return HttpResponseNotFound('<h1>Error</h1>')
    return render(request,"recrutamento_novo.html",{'form':my_form})

def relatorio_lista_view(request):
    lista = Relatorios_recrutamento.objects.all()
    return render(request,"recrutamento_lista.html",{'lista':lista})

@login_required
def download_relatorio_recrutamento_view(request,relatorio_pk,*args,**kargs):
    object                = Relatorios_recrutamento.objects.get(pk=relatorio_pk)
    file_path = object.documento.url[1:]
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response      = HttpResponse(fh.read(), content_type="")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseNotFound('<h1>Error</h1>')
