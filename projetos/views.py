from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.static import serve
import os
from django.conf import settings
from django.urls import path
import docx

def relatorio(request):
    documento = docx.Document()
    documento.add_paragraph('oi')
    documento.save("oi.docx")
    print(os.getcwd())
    return render(request,"home1.html",{})
