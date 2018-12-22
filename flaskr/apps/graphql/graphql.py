import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flaskr.models.warranty import Warranty
from flaskr.models.trunk import Trunk


class DefaultObjectType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    @classmethod
    def get_node(cls, info, id):
        return cls.get_query(info).filter(
            cls._meta.model.id==id
        ).first()


class WarrantyType(DefaultObjectType):
    class Meta:
        model = Warranty


class TrunkType(DefaultObjectType):
    class Meta:
        model = Trunk


class Query(graphene.ObjectType):
    warranties = graphene.List(lambda: WarrantyType, id=graphene.Int())

    def resolve_warranties(self, info, *args, **kwargs):
        query = WarrantyType.get_query(info)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(getattr(Warranty, key) == value).all()
        return query

    trunks = graphene.List(lambda: TrunkType, id=graphene.Int())

    def resolve_trunks(self, info, *args, **kwargs):
        query = TrunkType.get_query(info)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(getattr(Trunk, key) == value).all()
        return query


schema = graphene.Schema(query=Query)
