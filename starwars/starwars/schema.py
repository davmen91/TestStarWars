from graphene import Schema, ObjectType, Field
import applications.person.schema as person
import applications.planet.schema as planet
import applications.film.schema as film


class Query(person.Query, planet.Query, film.Query, ObjectType):
    """ Consultas de planetas, personajes y películas """
    pass

class Mutation(person.Mutation, planet.Mutation, film.Mutation, ObjectType):
    """ Mutaciones para crear planetas, personajes y películas """
    pass

schema = Schema(query=Query, mutation=Mutation)
