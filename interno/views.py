from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.static import serve
import os
from django.conf import settings
from django.urls import path
import docx
from django.conf.urls.static import static
from django.conf import settings




def relatorio(request):
    relatorio_path = os.getcwd() + settings.MEDIA_URL + '/relatorios'
    aux_path = os.getcwd()
    os.chdir(relatorio_path)
    print(os.getcwd())
    # template = docx.Document("template.docx")
# #
#     pass
    os.chdir(aux_path)
    return render(request,"home123.html",{})
