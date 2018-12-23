from . import marshmallow as ma
from flaskr.models.warranty import Warranty


class WarrantySchema(ma.ModelSchema):
    class Meta:
        model = Warranty
