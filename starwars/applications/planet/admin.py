from django.contrib import admin
from .models import Planet
# Register your models here.


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'diameter', 'climate', 'gravity', 'population')
    ordering = ('name',)