from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.processos_home_view, name = 'home_url'),
    path('search/', views.lista_procura_view,name='procura_url'),
    path('download/<int:processo_pk>/', views.download_processo_view, name='processos_download_url'),
    path('<slug:departamento_slug>/', views.lista_processos_view ,name='departamento_url'),
]
