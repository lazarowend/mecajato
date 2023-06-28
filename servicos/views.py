from django.shortcuts import render
from django.urls import reverse
from .forms import FormServico
from django.contrib import messages
from .models import Servico
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, FileResponse
from fpdf import FPDF
from io import BytesIO

# Create your views here.

def novo_servico(request):
    if request.method == 'GET':
        form = FormServico()
        context = {
            'form': form,
        }
        return render(request, 'novo_servico.html', context)
    elif request.method == 'POST':
        print('aqui')
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            form = FormServico()
            context = {
                'form': form,
            }
            messages.success(request, "Cliente cadastrado com Sucesso!")
            return render(request, 'novo_servico.html', context)
        else:
            messages.warning(request, "Dados inválidos!")
            context = {
                'form': form,
            }
            return render(request, 'novo_servico.html', context)

def listar_servico(request):
    if request.method == 'GET':
        pesquisa = request.GET.get('pesquisa')
        if not pesquisa:
            servicos = Servico.objects.all()
            context = {
                'servicos': servicos
            }
            return render(request, 'listar_servico.html', context)
        elif len(pesquisa) >= 1:
            servicos = Servico.objects.filter(Qtitulo__icontains=pesquisa)
            context = {
                'servicos': servicos
            }
            return render(request, 'listar_servico.html', context)
            pass
    elif request.method == 'POST':
        pass

def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    context = {
        'servico':servico
    }
    return render(request, 'servico.html', context)


def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.set_fill_color(240,240,240)

    pdf.cell(35, 10, 'Cliente: ', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)

    pdf.cell(45, 10, 'Manutenções: ', 1, 0, 'L', 1)
    categoria_manutencao = servico.categoria_manutencao.all()
    for i, manutencao in enumerate(categoria_manutencao):
        pdf.cell(0, 10, f'{manutencao.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == (len(categoria_manutencao) - 1):
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(50, 10, 'Data de Inicio: ', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)

    pdf.cell(50, 10, 'Data de Entrega: ', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_fim}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Protocolo: ', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 1)


    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f'os-{servico.protocolo}.pdf')