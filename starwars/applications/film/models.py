from django.db import models

from applications.planet.models import Planet
from applications.person.models import Person

class Film(models.Model):
    title = models.CharField(max_length=100, help_text="Título de la película")
    episode_id = models.IntegerField(help_text="N° de episodio correspondiente")
    opening_crawl = models.TextField(max_length=1000, help_text="Descripción introductoria")
    director = models.CharField(max_length=100, help_text="Director de la película")
    producer = models.CharField(max_length=100, help_text="Productor de la película")
    release_date = models.DateField(help_text="Fecha de lanzamiento")
    people = models.ManyToManyField(
        Person,
        related_name="film_person",
        blank=True, 
        help_text="Personajes que aparecen en la película"
    )
    planets = models.ManyToManyField(
        Planet,
        related_name="film_planet",
        blank=True,
        help_text="Planetas que aparecen en la película"
    )

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.title
