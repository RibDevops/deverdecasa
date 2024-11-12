from django.contrib import admin
from django.urls import path, include
from .views import *
from django.urls import path
from . import views  # Importe suas views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('index', index, name="index"),
    path('logout/', views.logout_view, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),


]