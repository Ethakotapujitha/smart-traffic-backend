import graphene
from graphene_django import DjangoObjectType
from .models import Signal

class SignalType(DjangoObjectType):
    class Meta:
        model = Signal
        fields = ("id", "signalStatus", "trafficCondition", "latitude", "longitude")

class Query(graphene.ObjectType):
    all_signals = graphene.List(SignalType)

    def resolve_all_signals(root, info):
        return Signal.objects.all()

schema = graphene.Schema(query=Query)












 