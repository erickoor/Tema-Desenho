from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tema_desenho, name='tema_desenho'),
    path('gerenciar_tema/', views.gerenciar_tema, name='gerenciar_tema'),
    path('excluir_tema/<str:id>', views.excluir_tema, name='excluir_tema'),
    path('sorteio/', views.sorteio, name='sorteio')
]
