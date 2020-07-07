from django.shortcuts import render, redirect
from .models import Endereco
from datetime import datetime


def index(request):
    enderecos = Endereco.objects.all()

    return render(request, 'index.html', { 
        'enderecos': enderecos 
    })

def cadastro_endereco(request):
    if request.method == 'GET':
        return render(request, 'cadastra-endereco.html')
    elif request.method == 'POST':
        rua = request.POST.get('rua', None)
        bairro = request.POST.get('bairro', None)
        numero = request.POST.get('numero', None)
        complemento = request.POST.get('complemento', None)
        descricao = request.POST.get('descricao', None)
        cidade = request.POST.get('cidade', None)
        uf = request.POST.get('uf', None)
        cep = request.POST.get('cep', None)
        date_endereco = datetime.now()

        Endereco.objects.create(
            rua = rua,
            bairro = bairro,
            numero = numero,
            complemento = complemento,
            descricao = descricao,
            cidade = cidade,
            uf = uf,
            cep = cep,
            date_endereco = date_endereco,
        )
    
    return redirect(index)