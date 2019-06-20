from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile')
    #path('signup/',views.signup_view,name="signup"),
]
