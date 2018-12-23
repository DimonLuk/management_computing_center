from flaskr.models.trunk import Trunk
from flaskr.models.ram import Ram
from flaskr.models.processor import Processor
from flaskr.models.motherboard import Motherboard
from flaskr.models.computer import Computer
from flaskr.models.manufacturer import Manufacturer
from flaskr.models.warranty import Warranty
from flaskr.models.component_meta_info import ComponentMetaInfo
from graphene_sqlalchemy import SQLAlchemyObjectType


class ComponentMetaInfoType(SQLAlchemyObjectType):
    class Meta:
        model = ComponentMetaInfo


class WarrantyType(SQLAlchemyObjectType):
    class Meta:
        model = Warranty


class TrunkType(SQLAlchemyObjectType):
    class Meta:
        model = Trunk


class RamType(SQLAlchemyObjectType):
    class Meta:
        model = Ram


class ProcessorType(SQLAlchemyObjectType):
    class Meta:
        model = Processor


class MotherboardType(SQLAlchemyObjectType):
    class Meta:
        model = Motherboard


class ComputerType(SQLAlchemyObjectType):
    class Meta:
        model = Computer


class ManufacturerType(SQLAlchemyObjectType):
    class Meta:
        model = Manufacturer
