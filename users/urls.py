from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit/', views.altera_dados_view, name='edit'),
    path('password/', views.change_password, name='change_password'),
    path('all/',views.mostra_view,name='mostra_todos'),
    path('<slug:username_slug>/',views.mostra_profile_view,name='profile_outro')
]
