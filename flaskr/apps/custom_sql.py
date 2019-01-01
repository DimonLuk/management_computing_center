from flask import Blueprint, request
from flaskr.models import get_db_session
import simplejson as json


bp = Blueprint('custom', __name__, url_prefix='/custom')


@bp.route('/customsql', methods=('POST',))
def process_sql():
    if request.method == 'POST':
        with get_db_session() as session:
            query_result = session.execute(request.json.get('sql_query'))
            column_names = query_result.keys()
            column_values = []
            for row in query_result.fetchall():
                obj = {}
                for key_index in range(len(column_names)):
                    obj[column_names[key_index]] = row[key_index]
                column_values.append(obj)
            response = {
                'column_names': column_names,
                'column_values': column_values
            }
            return json.dumps(response, use_decimal=True)
