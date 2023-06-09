from django.http import HttpResponse
from datetime import date
from django.shortcuts import redirect, render
from core.forms import TaskForm
from core.models import TaskModel


def cadastro(request):
    if request.method == 'POST':
        form_atividade = TaskForm(request.POST)
        if form_atividade.is_valid():
            TaskModel.objects.create(**form_atividade.cleaned_data)
            #return render(request, 'index.html')
            return redirect('index')
        else:
            contexto = {
                'form_atividade': form_atividade
            }
            return render (request, 'cadastro.html', contexto)
    else:
        contexto = {
            'form_atividade': TaskForm()
        }
        return render (request, 'cadastro.html', contexto)
    
#def verifica_atividade(request):
   # qs = TaskModel.objects.all()
   # data_atual = date.today()
   # nome_default = "Não tem tarefas hoje. Aproveite o dia!"
    
   # for atividade in qs:
        
   #     if atividade.dia_atividade == data_atual.day and atividade.mes_atividade == data_atual.month:
   #         nome_default = atividade.nome_atividade
            
    #contexto = {
    #    'atividade': nome_default
      
   # }
    #return render (request, 'index.html', contexto)

def verifica_atividade(request):
    data_atual = date.today()
    atividade = TaskModel.objects.filter(dia_atividade=data_atual.day, mes_atividade=data_atual.month).first()
    nome_default = atividade.nome_atividade if atividade else "Não tem tarefas hoje. Aproveite o dia!"
    contexto = {
        'atividade': nome_default
    }
    return render(request, 'index.html', contexto)
