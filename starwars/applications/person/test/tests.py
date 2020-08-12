from django.test import TestCase
from graphene import Schema, ObjectType

import applications.person.schema as person
import applications.planet.schema as planet
import applications.person.test.data as data


class Query(planet.Query, person.Query, ObjectType):
    pass

class Mutation(person.Mutation, ObjectType):
    pass


class AnExample(TestCase):

    fixtures = ['applications/planet/test/fixtures.json','applications/person/test/fixtures.json']

    def setUp(self):
        super().setUp()
        self.query = data.query
        self.mutation = data.create_mutation

    def test_query_person(self):
        schema = Schema(query=Query)
        result = schema.execute(self.query)
        print(f"Resultado Query {result}")
        self.assertIsNone(result.errors)
        self.assertDictEqual(data.result_query, result.data)

    def test_create_person(self):
        schema = Schema(mutation=Mutation) 
        result = schema.execute(self.mutation, variable_values=data.input_mutation)
        print(f"Resultado Mutation {result}")
        self.assertIsNone(result.errors)
