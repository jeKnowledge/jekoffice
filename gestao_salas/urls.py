from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.salas_home_view, name = 'salas_urls'),
    path('<slug:sala_slug>/',views.salas_rental_view,name = 'rental'),
]
