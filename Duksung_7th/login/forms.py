from django import forms
from django.contrib.auth.models import User
from .models import Login
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['u_id','u_pw']