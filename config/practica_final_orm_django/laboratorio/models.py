from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, null=True, blank=True) # Nuevo campo
    pais = models.CharField(max_length=255, null=True, blank=True)    # Nuevo campo

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(null=True, blank=True)
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def clean(self):
        if self.f_fabricacion:
            if self.f_fabricacion < date(2015, 1, 1):
                raise ValidationError("La fecha de fabricación no puede ser anterior a 2015.")

    def __str__(self):
        return self.nombre