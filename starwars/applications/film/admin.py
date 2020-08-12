from django.contrib import admin
from .models import Film
# Register your models here.


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'episode_id', 'director', 'producer', 'release_date')
    ordering = ('title',)
    raw_id_fields = ('people', 'planets')