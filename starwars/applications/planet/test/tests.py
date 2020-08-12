from django.test import TestCase
from graphene import Schema, ObjectType

import applications.planet.schema as planet
import applications.planet.test.data as data


class Query(planet.Query, ObjectType):
    pass

class Mutation(planet.Mutation, ObjectType):
    pass


class AnExample(TestCase):

    fixtures = ['applications/planet/test/fixtures.json']

    def setUp(self):
        super().setUp()
        self.query = data.query
        self.mutation = data.create_mutation

    def test_query_planet(self):
        schema = Schema(query=Query)
        result = schema.execute(self.query)
        print(f"Resultado Query {result}")
        self.assertIsNone(result.errors)
        self.assertDictEqual(data.result_query, result.data)

    def test_create_planet(self):
        schema = Schema(mutation=Mutation) 
        result = schema.execute(self.mutation, variable_values=data.input_mutation)
        print(f"Resultado Mutation {result}")
        self.assertIsNone(result.errors)
