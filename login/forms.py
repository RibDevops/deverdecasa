from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from.models import User

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)