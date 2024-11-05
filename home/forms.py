from django import forms

class BTUCalculationForm(forms.Form):
    wall_material = forms.CharField(label='Material da Parede', max_length=100)
    wall_thickness = forms.FloatField(label='Espessura da Parede (em metros)')
    room_height = forms.FloatField(label='Altura do Local (em metros)')
    room_width = forms.FloatField(label='Largura do Local (em metros)')
    room_length = forms.FloatField(label='Comprimento do Local (em metros)')
    insulation_area = forms.FloatField(label='Área Isolada (em m²)', required=False)
    lamp_type = forms.CharField(label='Tipo de Lâmpada', max_length=100)
    lamp_quantity = forms.IntegerField(label='Quantidade de Lâmpadas')
    equipment_quantity = forms.IntegerField(label='Quantidade de Equipamentos')
    people_count = forms.IntegerField(label='Número de Pessoas no Local')
