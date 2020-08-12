from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import FilmNode, CreateFilm, UpdateFilm, DeleteFilm


class Query(object):
    film = relay.Node.Field(FilmNode)
    films = DjangoFilterConnectionField(FilmNode)


class Mutation(object):
    create_film = CreateFilm.Field()
    update_film = UpdateFilm.Field()
    delete_film = DeleteFilm.Field()
