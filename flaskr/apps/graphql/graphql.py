import graphene
from flaskr.models import get_db_session
from flaskr.models.warranty import Warranty
from flaskr.serializers.warranty_serializer import WarrantySerializer
from flask import Blueprint, request
import json
import datetime


bp = Blueprint('graphql', __name__, url_prefix='/graphql')


class Query(graphene.ObjectType):
    warranty = graphene.JSONString(id=graphene.Int())

    def resolve_warranty(self, info, id):
        with get_db_session() as session:
            warranty = session.query(Warranty).get(id)
            result = WarrantySerializer(warranty).json
            return result


schema = graphene.Schema(query=Query)


@bp.route('/query', methods=('POST',))
def process_query():
    result = schema.execute(request.data.decode('utf-8').replace('\'', ''))
    return result.data.get('warranty')
