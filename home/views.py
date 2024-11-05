import os
from django.shortcuts import render
from .forms import BTUCalculationForm

def calculate_btu(request):
    if request.method == 'POST':
        form = BTUCalculationForm(request.POST)
        if form.is_valid():
            # Coletando os dados do formulário
            wall_material = form.cleaned_data['wall_material']
            wall_thickness = form.cleaned_data['wall_thickness']
            room_height = form.cleaned_data['room_height']
            room_width = form.cleaned_data['room_width']
            room_length = form.cleaned_data['room_length']
            insulation_area = form.cleaned_data.get('insulation_area', 0)
            lamp_type = form.cleaned_data['lamp_type']
            lamp_quantity = form.cleaned_data['lamp_quantity']
            equipment_quantity = form.cleaned_data['equipment_quantity']
            people_count = form.cleaned_data['people_count']

            # Parâmetros adicionais (para fins de cálculo)
            T1 = 22  # Temperatura interna desejada em °C
            T2 = 35  # Temperatura externa em °C
            wall_area = 2 * (room_height * room_width + room_height * room_length)  # Área total das paredes
            k = 0.72  # Exemplo de condutividade térmica (tijolo)
            A = wall_area  # Área total das paredes

            # Calcular R (resistência térmica total da parede)
            R = wall_thickness / (k * A)

            # Calcular Q_calor (transferência de calor)
            Q_calor = (T1 - T2) / R

            # Calcular contribuição das lâmpadas
            power_per_lamp = 70  # Potência média de cada lâmpada em W
            Q_lampada = lamp_quantity * power_per_lamp * 3600  # Energia em Joules (W * s)

            # Calcular contribuição dos equipamentos
            power_per_equipment = 500  # Potência média por equipamento em W
            Q_equipamento = equipment_quantity * power_per_equipment * 3600

            # Calcular contribuição das pessoas
            power_per_person = 100  # Aproximadamente 100W por pessoa
            Q_pessoa = people_count * power_per_person * 3600

            # Calcular Q_total
            Q_total = Q_calor + Q_lampada + Q_equipamento + Q_pessoa

            # Adicionar 10% de margem de segurança
            Q_total *= 1.1

            # Converter Q_total para BTUs (1 Watt = 3.412 BTU/h)
            BTUs = Q_total / 3600 * 3.412  # Converte de Joules para BTU/h

            return render(request, 'home/btu_result.html', {'btu': BTUs})

    else:
        form = BTUCalculationForm()
    return render(request, 'home/btu_form.html', {'form': form})
