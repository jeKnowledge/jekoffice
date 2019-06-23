from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
from django.db.models import Q
from .models import Processos
from django.contrib.auth.decorators import login_required
from django.views.static import serve
import os
from django.conf import settings
from django.urls import path

@login_required
def processos_home_view(request, *args,**kargs):
    return render(request,"processos_home.html",{})


@login_required
def lista_processos_view(request, departamento_slug, *args, **kargs):
    search               = request.GET.get('search_box',None)
    print(search)
    if not search:
        query_set        = Processos.objects.filter(departamento = departamento_slug.upper())
    else:
        query_set        = Processos.objects.filter(Q(departamento = departamento_slug.upper()) & Q(nome__icontains = search) )
    if not query_set and not search:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request,"processos_lista.html",{'lista' : query_set})

@login_required
def lista_procura_view(request, *args,**kargs):
    search               = request.GET.get('search_box',None)
    print(search)
    if not search:
        query_set        = Processos.objects.all()
    else:
        query_set        = Processos.objects.filter(Q(departamento__icontains = search) | Q(nome__icontains = search))
    return render(request,"processos_lista.html",{'lista':query_set})
#falta acabar a parte do search

@login_required
def download_processo_view(request,processo_pk,*args,**kargs):
    try:
        object                = Processos.objects.get(pk=processo_pk)
        file_path = object.documento.url[1:]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response      = HttpResponse(fh.read(), content_type="")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
    except:
        pass
    return HttpResponseNotFound('<h1>Error</h1>')
