from django.db import models

class BTUCalculation(models.Model):
    wall_material = models.CharField(max_length=100)
    wall_thickness = models.FloatField()  # espessura em metros
    room_height = models.FloatField()     # altura em metros
    room_width = models.FloatField()      # largura em metros
    room_length = models.FloatField()     # comprimento em metros
    insulation_area = models.FloatField() # área isolada em m²
    lamp_type = models.CharField(max_length=100)
    lamp_quantity = models.IntegerField()
    equipment_quantity = models.IntegerField()
    people_count = models.IntegerField()
    btu_required = models.FloatField(blank=True, null=True)  # Será preenchido após o cálculo
