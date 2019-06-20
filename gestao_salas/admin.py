from django.contrib import admin
from .models import Salas,Rentals
from django.contrib.auth.admin import UserAdmin
from .models import Rentals

# Register your models here.



class RentalsAdmin(admin.ModelAdmin):
    model = Rentals
    list_display = ['dia','sala','data_inicio','data_final']
    ordering= ('dia','data_inicio','data_final')

admin.site.register(Salas)
admin.site.register(Rentals,RentalsAdmin)
