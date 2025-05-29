import graphene
from graphene_django.types import DjangoObjectType
from .models import Instrument

class InstrumentType(DjangoObjectType):
    class Meta:
        model = Instrument

class Query(graphene.ObjectType):
    all_instruments = graphene.List(InstrumentType)

    def resolve_all_instruments(root, info):
        return Instrument.objects.all()

schema = graphene.Schema(query=Query)
