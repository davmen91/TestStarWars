from django.contrib import admin
from .models import Person

# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'height', 'skin_color', 'birth_year', 'gender')
    ordering = ('name', )
    raw_id_fields = ('homeworld',)
