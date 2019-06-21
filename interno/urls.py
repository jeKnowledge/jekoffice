from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.relatorio_novo_view, name='criar_relatorios'),
    path('', views.relatorio_lista_view, name='relatorios'),
    path('download/<int:relatorio_pk>/', views.download_relatorio_recrutamento_view,name='download_recrutamento'),
]
