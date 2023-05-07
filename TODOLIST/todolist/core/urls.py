from django.urls import path
from . import views

urlpatterns = [
    path('',views.verifica_atividade, name="index"),
    path('cadastro/',views.cadastro, name='core_cadastro'),
]