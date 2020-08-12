from django.db import models

# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=100, help_text="Nombre del planeta")
    rotation_period = models.CharField(max_length=40, help_text="La cantidad de horas estándar que le toma a este planeta completar una sola rotación sobre su eje")
    orbital_period = models.CharField(max_length=40, help_text="La cantidad de días estándar que le toma a este planeta completar una sola órbita de su estrella local")
    diameter = models.CharField(max_length=40, help_text="Diametro del planeta en kms")
    climate = models.CharField(max_length=40, help_text="Clima del planeta")
    gravity = models.CharField(max_length=40, help_text="Un número que denota la gravedad de este planeta, donde '1' es normal o 1 estándar G. '2' es dos veces o 2 G estándar. '0.5' es la mitad o 0.5 G estándar")
    terrain = models.CharField(max_length=40, help_text="Terreno del planeta")
    surface_water = models.CharField(max_length=40, help_text="El porcentaje de la superficie del planeta que corresponde a agua")
    population = models.CharField(max_length=40, help_text="La población promedio de seres en el planeta")

    class Meta:
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'

    def __str__(self):
        return self.name
