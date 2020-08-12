from graphene import relay, Field, String, Int
from graphene_django import DjangoObjectType

from .models import Planet


class PlanetNode(DjangoObjectType):
    class Meta:
        model = Planet
        description = "Planetas de Star Wars"
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['exact', 'icontains']
        }


class UpdatePlanet(relay.ClientIDMutation):
    """ Actualizar un planeta """

    planet = Field(PlanetNode)

    class Input:
        planet_id = Int()
        rotation_period = String()
        orbital_period = String()
        climate = String()
        gravity = String()
        terrain = String()
        surface_water = String()
        population = String()

    def mutate_and_get_payload(self, info, **input):
        planet = Planet.objects.get(id=input.get('planet_id'))
        planet.rotation_period = input.get('rotation_period')
        planet.orbital_period = input.get('orbital_period')
        planet.climate = input.get('climate')
        planet.gravity = input.get('gravity')
        planet.terrain = input.get('terrain')
        planet.surface_water = input.get('surface_water')
        planet.population = input.get('population')

        planet.save()
        return UpdatePlanet(planet=planet)


class DeletePlanet(relay.ClientIDMutation):
    """ Eliminar un planeta """

    planet_id = Int()

    class Input:
        planet_id = Int(required=True)

    def mutate_and_get_payload(self, info, planet_id):
        planet = Planet.objects.get(id=planet_id)
        planet.delete()

        return DeletePlanet(planet_id=planet_id)


class CreatePlanet(relay.ClientIDMutation):
    """ Crear un planeta """

    planet = Field(PlanetNode)

    class Input:
        name = String()
        rotation_period = String()
        orbital_period = String()
        diameter = String()
        climate = String()
        gravity = String()
        terrain = String()
        surface_water = String()
        population = String()

    def mutate_and_get_payload(self, info, **input):
        planet = Planet(
            name=input.get('name'),
            rotation_period=input.get('rotation_period'),
            orbital_period=input.get('orbital_period'),
            diameter=input.get('diameter'),
            climate=input.get('climate'),
            gravity=input.get('gravity'),
            terrain=input.get('terrain'),
            surface_water=input.get('surface_water'),
            population=input.get('population'),
        )

        planet.save()
        return CreatePlanet(planet=planet)
