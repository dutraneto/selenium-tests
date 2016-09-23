from django.shortcuts import render, redirect, get_object_or_404

from crud_app.forms import FormPessoa, FormPertence
from .models import Pessoa, Pertence


def listagem(request):
    pessoa = Pessoa.objects.all().order_by('nome_pessoa')
    return render(request, 'crud_app/listagem.html', {'pessoa': pessoa})

def detalhes(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if Pertence.objects.filter(pessoa_fk=pk).exists():
        pertences = Pertence.objects.filter(pessoa_fk=pk).order_by('nome_pertence')
    else:
        pertences = 'Nenhuma informação cadastrada'
    return render(request, 'crud_app/detalhes.html', {'pessoa': pessoa, 'pertences': pertences})

def cadastrarPessoa(request):
    if request.method == 'POST':
        form = FormPessoa(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.save()
            return redirect('detalhes', pk=pessoa.pk)
    else:
        form = FormPessoa()
    return render(request, 'crud_app/cadastrarPessoa.html', {'form':form})

def cadastrarPertences(request, pk):
    if request.method == 'POST':
        form = FormPertence(request.POST)
        if form.is_valid():
            pertence = form.save(commit=False)
            pertence.pessoa_fk = Pessoa.objects.get(pk=pk)
            pertence.save()
            return redirect('detalhes', pk=pk)
    else:
        form = FormPertence()
    return render(request, 'crud_app/cadastrarPertences.html', {'form':form})

def editarPessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        form = FormPessoa(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.save()
            return redirect('detalhes', pk=pessoa.pk)
    else:
        form = FormPessoa(instance=pessoa)
    return render(request, 'crud_app/editarPessoa.html', {'form':form, 'nome_pessoa':pessoa.nome_pessoa})

def excluir(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()
    return redirect('listagem')