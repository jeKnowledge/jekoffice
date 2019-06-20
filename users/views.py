from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def signup_view(request,*args,**kwargs):
#     form = Raw_UserForm()
#     if request.method == 'POST':
#         form = Raw_UserForm(request.POST)
#         if form.is_valid():
#             CustomUser.objects.create(**form.cleaned_data)
#     return render(request,"signup.html",{'form':form})

def profile_view(request, *args, **kwargs):
    #falta botao edit
    return render(request,"profile.html")
