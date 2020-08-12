from django.db import models
from applications.planet.models import Planet
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=80, help_text="Nombre del personaje")
    height = models.CharField(max_length=5, blank=True, help_text="Estatura del personaje")
    mass = models.CharField(max_length=3, blank=True, help_text="Peso del personaje en kg")
    hair_color = models.CharField(max_length=20, blank=True, help_text="Color del cabello")
    skin_color = models.CharField(max_length=20, blank=True, help_text="Color de piel")
    eye_color = models.CharField(max_length=20, blank=True, help_text="Color de ojos")
    birth_year = models.CharField(max_length=10, blank=True, help_text="Fecha de nacimiento según el estandar del universo de Star Wars, donde BBY y ABY corresponden a 'Before the Battle of Yavin' y 'After the Battle of Yavin'")
    gender = models.CharField(max_length=40, blank=True, help_text="Genero del personaje")
    homeworld = models.ForeignKey(Planet, related_name="residents", on_delete=models.CASCADE, help_text="Planeta en el que nació o vive el personaje")
    create_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación en BD")

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name
