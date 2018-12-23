from .types import (
    TrunkType,
    ComponentMetaInfoType,
    MotherboardType,
    RamType,
    ProcessorType,
    ManufacturerType,
    ComputerType,
    WarrantyType
)
from .attributes import (
    TrunkAttribute,
    ComponentMetaInfoAttribute,
    MotherboardAttribute,
    RamAttribute,
    ProcessorAttribute,
    ManufacturerAttribute,
    ComputerAttribute,
    WarrantyAttribute
)
from flaskr.models.warranty import Warranty
from flaskr.models.trunk import Trunk
from flaskr.models.computer import Computer
from flaskr.models.manufacturer import Manufacturer
from flaskr.models.motherboard import Motherboard
from flaskr.models.processor import Processor
from flaskr.models.ram import Ram
from flaskr.models.component_meta_info import ComponentMetaInfo


FIELDS_TO_RETRIEVE = (
    {
        'model': Warranty,
        'type': WarrantyType,
        'attribute': WarrantyAttribute,
    },
    {
        'model': Trunk,
        'type': TrunkType,
        'attribute': TrunkAttribute,
    },
    {
        'model': Computer,
        'type': ComputerType,
        'attribute': ComputerAttribute,
    },
    {
        'model': Manufacturer,
        'type': ManufacturerType,
        'attribute': ManufacturerAttribute,
    },
    {
        'model': Motherboard,
        'type': MotherboardType,
        'attribute': MotherboardAttribute,
    },
    {
        'model': Processor,
        'type': ProcessorType,
        'attribute': ProcessorAttribute,
    },
    {
        'model': Ram,
        'type': RamType,
        'attribute': RamAttribute,
    },
    {
        'model': ComponentMetaInfo,
        'type': ComponentMetaInfoType,
        'attribute': ComponentMetaInfoAttribute
    },
)
