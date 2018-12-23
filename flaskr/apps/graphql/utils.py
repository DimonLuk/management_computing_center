from .types import (
    TrunkType,
    ComponentMetaInfoType, # NOQA
    MotherboardType,
    RamType,
    ProcessorType,
    ManufacturerType,
    ComputerType,
    WarrantyType
)
from flaskr.models.warranty import Warranty
from flaskr.models.trunk import Trunk
from flaskr.models.computer import Computer
from flaskr.models.manufacturer import Manufacturer
from flaskr.models.motherboard import Motherboard
from flaskr.models.processor import Processor
from flaskr.models.ram import Ram


FIELDS_TO_RETRIEVE = (
    {
        'model': Warranty,
        'type': WarrantyType
    },
    {
        'model': Trunk,
        'type': TrunkType
    },
    {
        'model': Computer,
        'type': ComputerType
    },
    {
        'model': Manufacturer,
        'type': ManufacturerType
    },
    {
        'model': Motherboard,
        'type': MotherboardType
    },
    {
        'model': Processor,
        'type': ProcessorType
    },
    {
        'model': Ram,
        'type': RamType
    },
)
