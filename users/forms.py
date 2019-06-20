from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name  = forms.CharField(label='First Name',
                    widget=forms.TextInput())
    last_name   = forms.CharField(label='Last Name')
    username    = forms.Field(widget=forms.TextInput(attrs={'class':'form-control'}))
    email       = forms.Field(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1   = forms.Field(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2   = forms.Field(label='Password Confirmation',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','password1',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
