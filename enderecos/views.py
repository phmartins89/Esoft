from django.shortcuts import render, redirect
from .models import Endereco
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
import json    


def index(request):
    enderecos = Endereco.objects.all()

    return render(request, 'index.html', { 
        'enderecos': enderecos 
    })

def recuperar_endereco(request):
    data = serializers.serialize("json", Endereco.objects.filter(cep=request.GET.get('cep', '')))
    return JsonResponse(json.loads(data), safe=False)

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