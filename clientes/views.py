import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro, Cliente
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages

# Create your views here.
    
def clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes})
    
    elif request.method == 'POST':

        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            context = {
                'nome': nome,
                'email': email,
                'sobrenome': sobrenome,
                'carros': zip(carros, placas, anos)
            }
            return render(request, 'clientes/clientes.html', context)

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            context = {
                'nome': nome,
                'cpf': cpf,
                'sobrenome': sobrenome,
                'carros': zip(carros, placas, anos)
            }
            return render(request, 'clientes/clientes.html', context)
        
        cliente = Cliente(nome=nome, sobrenome=sobrenome, email=email, cpf=cpf)

        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):

            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()

        messages.success(request, "Cliente cadastrado com Sucesso!")
        
        return redirect('clientes')



def att_cliente(request):
    id = request.POST.get('id_cliente')

    cliente = Cliente.objects.filter(id=id)
    carros = Carro.objects.filter(cliente_id=id)

    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    carros_json = json.loads(serializers.serialize('json', carros))
    cliente_id = json.loads(serializers.serialize('json', carros))[0]['pk']

    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]
    data = {
        'cliente': cliente_json,
        'carros': carros_json,
        'id_cliente': cliente_id,
    }
    return JsonResponse(data)

@csrf_exempt
def update_carro(resquest, id):
    if resquest.method == 'POST':
        nome_carro = resquest.POST.get('carro')
        placa = resquest.POST.get('placa')
        ano = resquest.POST.get('ano')

        verifica_carros = Carro.objects.filter(placa=placa).exclude(id=id)
        if verifica_carros.exists():
            return HttpResponse('Já existe essa placa')

        carro = Carro.objects.get(id=id)
        carro.carro = nome_carro
        carro.ano = ano
        carro.placa = placa
        carro.save()
        return HttpResponse('alterado com sucesso')

        
def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        messages.success(request, "Carro apagado com sucesso!")
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        messages.danger(request, "Erro ao apagar carro!")
        return redirect(reverse('clientes'))


def update_cliente(request, id):
    id = (id - 1)
    body = json.loads(request.body)
    cpf = body['cpf']
    cliente = Cliente.objects.filter(cpf=cpf).exclude(id=id)

    if cliente.exists():
        return JsonResponse({'statuss': '400'})    
    
    cliente = get_object_or_404(Cliente, id=id)
    try:
        cliente.nome = body['nome']
        cliente.sobrenome = body['sobrenome']
        cliente.email = body['email']
        cliente.cpf = body['cpf']
        cliente.save()
        return JsonResponse({'status': '200'})
    except:
        return JsonResponse({'statuss': '400'})

