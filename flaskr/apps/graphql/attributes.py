import graphene


class DefaultComponentAttributeMixin:
    component_meta_info_id = graphene.Int()


class ComponentMetaInfoAttribute:
    serial_number = graphene.String()
    manufacturer_id = graphene.Int()
    warranty_id = graphene.Int()
    status = graphene.String()


class ComputerAttribute:
    room = graphene.String()
    trunk_id = graphene.Int()
    motherboard_id = graphene.Int()
    ram_id = graphene.Int()
    processor_id = graphene.Int()


class ManufacturerAttribute(DefaultComponentAttributeMixin):
    title = graphene.String()
    address = graphene.String()
    phone_number = graphene.String()


class MotherboardAttribute(DefaultComponentAttributeMixin):
    form_factor = graphene.String()
    chipset = graphene.String()
    pci_slots = graphene.Int()
    used_pci_slots = graphene.Int()
    ram_slots = graphene.Int()
    used_ram_slots = graphene.Int()


class ProcessorAttribute(DefaultComponentAttributeMixin):
    cors = graphene.Int()
    l1_cache = graphene.Int()
    l2_cache = graphene.Int()
    l3_cache = graphene.Int()


class RamAttribute(DefaultComponentAttributeMixin):
    capacity = graphene.Int()
    frequency = graphene.Int()


class TrunkAttribute(DefaultComponentAttributeMixin):
    width = graphene.Int()
    height = graphene.Int()
    form_factor = graphene.String()


class WarrantyAttribute:
    start_date = graphene.Date()
    end_date = graphene.Date()
