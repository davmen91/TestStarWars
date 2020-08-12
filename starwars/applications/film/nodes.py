from graphene import relay, Field, String, Int, List, ID
from graphene_django import DjangoObjectType
import datetime

from .models import Film, Person, Planet


class FilmNode(DjangoObjectType):
    class Meta:
        model = Film
        description = "Peliculas de Star Wars"
        interfaces = (relay.Node, )
        filter_fields = {
            'title': ['exact', 'icontains']
        }


class UpdateFilm(relay.ClientIDMutation):
    """ Actualizar una película """

    film = Field(FilmNode)

    class Input:
        film_id = Int(required=True)
        episode_id = Int()
        opening_crawl = String()
        director = String()
        producer = String()
        release_date = String()

    def mutate_and_get_payload(self, info, **input):
        film = Film.objects.get(id=input.get('film_id'))
        film.episode_id = input.get('episode_id')
        film.opening_crawl = input.get('opening_crawl')
        film.director = input.get('director')
        film.producer = input.get('producer')
        film.release_date = input.get('release_date')

        film.save()
        return UpdateFilm(film=film)


class DeleteFilm(relay.ClientIDMutation):
    """ Eliminar una película """

    film_id = Int()

    class Input:
        film_id = Int(required=True)

    def mutate_and_get_payload(self, info, film_id):
        film = Film.objects.get(id=film_id)
        film.delete()

        return DeleteFilm(film_id=film_id)


class CreateFilm(relay.ClientIDMutation):
    """ Crear una película """

    film = Field(FilmNode)

    class Input:
        title = String()
        episode_id = Int()
        opening_crawl = String()
        director = String()
        producer = String()
        release_date = String()
        people = List(ID)
        planets = List(ID)

    def mutate_and_get_payload(self, info, **input):
        print(input.get('people'))

        film = Film(
            title=input.get('title'),
            episode_id=input.get('episode_id'),
            opening_crawl=input.get('opening_crawl'),
            director=input.get('director'),
            producer=input.get('producer'),
            release_date=datetime.datetime.strptime(
                input.get('release_date'), '%Y-%m-%d'),
        )

        film.save()
        film.people.set(Person.objects.get(id=person_id)
                        for person_id in input.get('people'))
        film.planets.set(Planet.objects.get(id=planet_id)
                         for planet_id in input.get('planets'))

        return CreateFilm(film=film)
