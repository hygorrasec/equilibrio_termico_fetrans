from django.shortcuts import render
from .forms import BTUCalculationForm

def calculate_btu(request):
    # Dados iniciais para pré-preenchimento
    initial_data = {
        'room_width': 10,
        'room_length': 10,
        'solar_exposure': 'Sol Diretamente',
        'people_count': 2,
        'tv_count': 2,
        'computer_count': 2,
        'lamp_count': 2,
        'lamp_type': 'LED',
        'window_count': 2,
        'appliance_count': 2,
        'wall_material': 'Concreto',
        'wall_thickness': 0.4,
        'room_height': 3.0,
        'insulation_area': 10.0,
    }

    if request.method == 'POST':
        form = BTUCalculationForm(request.POST)
        if form.is_valid():
            # Coletando dados do formulário
            room_width = form.cleaned_data['room_width']
            room_length = form.cleaned_data['room_length']
            solar_exposure = form.cleaned_data['solar_exposure']
            people_count = form.cleaned_data['people_count']
            tv_count = form.cleaned_data['tv_count']
            computer_count = form.cleaned_data['computer_count']
            lamp_count = form.cleaned_data['lamp_count']
            lamp_type = form.cleaned_data['lamp_type']
            window_count = form.cleaned_data['window_count']
            appliance_count = form.cleaned_data['appliance_count']
            wall_material = form.cleaned_data['wall_material']
            wall_thickness = form.cleaned_data['wall_thickness']
            room_height = form.cleaned_data['room_height']
            insulation_area = form.cleaned_data.get('insulation_area', 0)

            # Cálculo solar
            room_area = room_width * room_length
            exposure_factor = {
                'Sol Diretamente': 800,
                'Sol Parcialmente': 700,
                'Sem Sol': 600,
            }
            solar_btu = room_area * exposure_factor[solar_exposure]

            # Potência das lâmpadas
            lamp_power = {
                'Incandescente': 80,
                'Fluorescente': 30,
                'LED': 15,
            }
            lamp_btu = lamp_count * lamp_power[lamp_type] * 3.412

            # Carga térmica interna
            btu_per_person = 600
            btu_per_tv = 200
            btu_per_computer = 300
            btu_per_window = 500
            btu_per_appliance = 500
            internal_btu = (
                people_count * btu_per_person +
                tv_count * btu_per_tv +
                computer_count * btu_per_computer +
                lamp_btu +
                window_count * btu_per_window +
                appliance_count * btu_per_appliance
            )

            # Cálculo de transferência térmica pelas paredes (Lei de Fourier)
            material_k = {
                'Concreto': 1.7,
                'Tijolo': 0.72,
                'Madeira': 0.13,
            }
            k = material_k.get(wall_material, 1.0)
            wall_area = 2 * (room_height * room_width + room_height * room_length)
            ceiling_area = room_width * room_length
            R_wall = wall_thickness / (k * wall_area)
            R_ceiling = wall_thickness / (k * ceiling_area)

            # Ajuste pela área isolada
            insulation_factor = 1 - (insulation_area / wall_area)
            Q_wall = ((35 - 22) / R_wall) * insulation_factor
            Q_ceiling = ((35 - 22) / R_ceiling) * insulation_factor

            # BTU total
            total_btu = solar_btu + internal_btu + Q_wall + Q_ceiling
            total_btu *= 1.1  # Margem de segurança

            # Sugestões de aparelhos
            types_of_air_conditioners = [
                {'type': 'Ar-Condicionado de Janela', 'capacity': 7500},
                {'type': 'Ar-Condicionado Split', 'capacity': 9000},
                {'type': 'Ar-Condicionado Split Inverter', 'capacity': 12000},
                {'type': 'Ar-Condicionado Multi Split', 'capacity': 18000},
                {'type': 'Ar-Condicionado Cassete', 'capacity': 24000},
                {'type': 'Ar-Condicionado Piso-Teto', 'capacity': 36000},
                {'type': 'Ar-Condicionado Duto', 'capacity': 60000},
            ]

            suggestions = []
            remaining_btu = total_btu

            for air_conditioner in sorted(types_of_air_conditioners, key=lambda x: x['capacity'], reverse=True):
                quantity = remaining_btu // air_conditioner['capacity']
                if quantity > 0:
                    suggestions.append({
                        'type': air_conditioner['type'],
                        'capacity': air_conditioner['capacity'],
                        'quantity': int(quantity),
                    })
                    remaining_btu %= air_conditioner['capacity']

            # Formatação do BTU total
            formatted_btu = f"{total_btu:,.0f}".replace(",", ".")

            return render(request, 'home/btu_result.html', {'btu': formatted_btu, 'suggestions': suggestions})

    else:
        # Pré-preenchendo os campos do formulário
        form = BTUCalculationForm(initial=initial_data)
    return render(request, 'home/btu_form.html', {'form': form})
