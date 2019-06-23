from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm,EditaForm
from django.contrib.auth.decorators import login_required
import os

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



@login_required
def altera_dados_view(request, *args, **kwargs):
    user = CustomUser.objects.get(pk=request.user.pk)
    data = {'username': request.user.username,'cc_num':request.user.cc_num,'email':request.user.email,'mac_adress':request.user.mac_adress}
    my_form = EditaForm(initial=data)
    aux_path = None
    if(user.imagem):
        aux_path = user.imagem.path
    if request.method == 'POST':
        my_form = EditaForm(request.POST, request.FILES,instance=user)
        if my_form.is_valid():
            dados_form = my_form.cleaned_data
            if(request.FILES and aux_path):
                os.remove(aux_path)
            user.username = dados_form['username']
            user.email = dados_form['email']
            user.cc_num = dados_form['cc_num']
            user.mac_adress = dados_form['mac_adress']
            user.save()
            return redirect('edit')

    return render(request,"edita.html",{"form":my_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def mostra_view(request):
    query_set = CustomUser.objects.all()
    return render(request,'mostra_users.html',{'lista':query_set})

def mostra_profile_view(request,username_slug):
    user = get_object_or_404(CustomUser, username=username_slug)
    return render(request,'profile_user.html',{'user':user})
