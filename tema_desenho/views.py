from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tema_Novo
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from random import choice

def tema_desenho(request):
    return render(request, 'index.html')

def gerenciar_tema(request):
    if request.method == 'GET':
        tema = Tema_Novo.objects.all()
        return render(request, 'gerenciar_tema.html', {'temas': tema})
    elif request.method == 'POST':
        novo_tema = request.POST.get('cadastrar_tema')
        tema = Tema_Novo.objects.filter(nome_tema = novo_tema)
        if len(tema) == 0 and len(novo_tema) > 0:
            tema = Tema_Novo(nome_tema = novo_tema)
            tema.save()
            tema = Tema_Novo.objects.all()
            messages.add_message(request, constants.SUCCESS, 'Tema cadastrado com sucesso!')
            return render(request, 'gerenciar_tema.html', {'temas': tema})
        elif len(tema) > 0:
            messages.add_message(request, constants.WARNING, 'O tema que está tentando cadastrar já existe!')
            return redirect(reverse('gerenciar_tema'))
        elif len(novo_tema) <= 0:
            messages.add_message(request, constants.WARNING, 'Digite algum tema para ser cadastrado!')
            return redirect(reverse('gerenciar_tema'))
        
def excluir_tema(request, id):
    tema = get_object_or_404(Tema_Novo, id = id)
    tema.delete()
    messages.add_message(request, constants.SUCCESS, 'Tema excluído com sucesso!')
    return redirect(reverse('gerenciar_tema'))

def sorteio(request):
    lista_temas = []
    try:
        tema = Tema_Novo.objects.all()
        for temas in range(len(tema)):
            lista_temas.append(tema[temas])
            tema_selecionado = choice(lista_temas)
        print(tema_selecionado)
        return render(request, 'index.html', {'tema_selecionado': tema_selecionado})
    except:
        messages.add_message(request, constants.WARNING, 'Nenhum tema cadastrado!')
        return redirect(reverse('tema_desenho'))
    
    