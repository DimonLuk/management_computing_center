from .base_serializer import BaseSerializer
from flaskr.models.warranty import Warranty


class WarrantySerializer(BaseSerializer):
    class Meta:
        fields = '__all__'
        model = Warranty
