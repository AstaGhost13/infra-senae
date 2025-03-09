

from django.urls import path
from .views import CustomLoginView, SignUpView
from django.contrib.auth.views import LogoutView

app_name = 'account' 

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", SignUpView.as_view(), name="register"),
    
]