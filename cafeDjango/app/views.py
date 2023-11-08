from django.shortcuts import render
from . models import *
import csv
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')



def exibir_analises(request):
    analises_solo = AnaliseSolo.objects.all()
    context = {
        'analises_solo': analises_solo,
    }
    return render(request, 'analisesolo.html', context)

def exportar_analises_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="analises_solo.csv"'

    csv_writer = csv.writer(response)

    csv_writer.writerow(['pH', 'Textura', 'Matéria Orgânica (%)', 'Qtde Cálcio', 'Qtde Magnésio', 'Qtde Potássio'])

    analises_solo = AnaliseSolo.objects.all()

    for analise in analises_solo:
        csv_writer.writerow([
            analise.ph,
            analise.textura,
            analise.materia_organica_porcentagem,
            analise.qtde_Calcio,
            analise.qtde_Magnesio,
            analise.qtde_Potassio
        ])

    return response

def exibir_fazendas(request):
    fazendas = Fazenda.objects.all()
    context = {
        'fazendas': fazendas,
    }
    return render(request, 'fazendas.html', context)

def exibir_area(request):
    areasplantio = AreaPlantio.objects.all()
    context = {
        'areasplantio': areasplantio,
    }
    return render(request, 'areaplantio.html', context)

def exibir_talhoes(request):
    talhoes = Talhoes.objects.all()
    context = {
        'talhoes': talhoes,
    }
    return render(request, 'talhoes.html', context)



