from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import PlanetNode, CreatePlanet, UpdatePlanet, DeletePlanet


class Query(object):
    planet = relay.Node.Field(PlanetNode)
    planets = DjangoFilterConnectionField(PlanetNode)


class Mutation(object):
    create_planet = CreatePlanet.Field()
    update_planet = UpdatePlanet.Field()
    delete_planet = DeletePlanet.Field()
