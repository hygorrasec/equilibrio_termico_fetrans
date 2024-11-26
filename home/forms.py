from django import forms

class BTUCalculationForm(forms.Form):
    # Campos anteriores e novos
    room_width = forms.FloatField(label='Largura do Local (em metros)')
    room_length = forms.FloatField(label='Comprimento do Local (em metros)')
    EXPOSURE_CHOICES = [
        ('Sol Diretamente', 'Sol Diretamente'),
        ('Sol Parcialmente', 'Sol Parcialmente'),
        ('Sem Sol', 'Sem Sol'),
    ]
    solar_exposure = forms.ChoiceField(
        label='Nível de Exposição Solar',
        choices=EXPOSURE_CHOICES,
        widget=forms.Select
    )
    people_count = forms.IntegerField(label='Número de Pessoas no Local')
    tv_count = forms.IntegerField(label='Número de Televisores', initial=0)
    computer_count = forms.IntegerField(label='Número de Computadores', initial=0)
    lamp_count = forms.IntegerField(label='Número de Lâmpadas', initial=0)
    LAMP_CHOICES = [
        ('Incandescente', 'Incandescente'),
        ('Fluorescente', 'Fluorescente'),
        ('LED', 'LED'),
    ]
    lamp_type = forms.ChoiceField(
        label='Tipo de Lâmpada',
        choices=LAMP_CHOICES,
        widget=forms.Select
    )
    window_count = forms.IntegerField(label='Número de Janelas', initial=0)
    appliance_count = forms.IntegerField(label='Número de Eletrodomésticos', initial=0)
    wall_material = forms.ChoiceField(
        label='Material da Parede',
        choices=[
            ('Concreto', 'Concreto'),
            ('Tijolo', 'Tijolo'),
            ('Madeira', 'Madeira'),
        ],
        widget=forms.Select
    )
    wall_thickness = forms.FloatField(label='Espessura da Parede (em metros)', initial=0.4)
    room_height = forms.FloatField(label='Altura do Local (em metros)')
    insulation_area = forms.FloatField(label='Área Isolada (em m²)', required=False, initial=0.0)
