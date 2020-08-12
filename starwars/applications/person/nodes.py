from graphene import relay, Field, String, Int, ID
from graphene_django import DjangoObjectType

from .models import Person, Planet

class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        description = "Personajes de Star Wars"
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['exact', 'icontains']
        }


class UpdatePerson(relay.ClientIDMutation):
    """ Actualizar un personaje """

    person = Field(PersonNode)

    class Input:
        person_id = Int(required=True)
        height = String()
        mass = String()
        hair_color = String()
        skin_color = String()
        eye_color = String()

    def mutate_and_get_payload(self, info, **input):
        person = Person.objects.get(id=input.get('person_id'))
        person.height = input.get('height')
        person.mass = input.get('mass')
        person.hair_color = input.get('hair_color')
        person.skin_color = input.get('skin_color')
        person.eye_color = input.get('eye_color')

        person.save()
        return UpdatePerson(person=person)


class DeletePerson(relay.ClientIDMutation):
    """ Eliminar un personaje """

    person_id = Int()

    class Input:
        person_id = Int(required=True)

    def mutate_and_get_payload(self, info, person_id):
        person = Person.objects.get(id=person_id)
        person.delete()

        return DeletePerson(person_id=person_id)


class CreatePerson(relay.ClientIDMutation):
    """ Crear un personaje """

    person = Field(PersonNode)

    class Input:
        name = String()
        height = String()
        mass = String()
        hair_color = String()
        skin_color = String()
        eye_color = String()
        birth_year = String()
        gender = String()
        homeworld = ID()

    def mutate_and_get_payload(self, info, **input):
        planet = Planet.objects.get(id=input.get('homeworld'))
        person = Person(
            name=input.get('name'),
            height=input.get('height'),
            mass=input.get('mass'),
            hair_color=input.get('hair_color'),
            skin_color=input.get('skin_color'),
            eye_color=input.get('eye_color'),
            birth_year=input.get('birth_year'),
            gender=input.get('gender'),
            homeworld=planet
        )

        person.save()
        return CreatePerson(person=person)
