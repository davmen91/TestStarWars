from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import PersonNode, CreatePerson, UpdatePerson, DeletePerson


class Query(object):
    person = relay.Node.Field(PersonNode)
    people = DjangoFilterConnectionField(PersonNode)


class Mutation(object):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()
