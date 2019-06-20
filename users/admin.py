from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

def make_super(modeladmin, request, queryset):
    queryset.update(is_super=True)
make_super.short_description = "Make Super"



class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username','email','departamento','is_super']
    actions = [make_super]
    ordering = ('departamento', 'username')
admin.site.register(CustomUser,CustomUserAdmin)
