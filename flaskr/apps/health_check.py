from flask import Blueprint, request
from flaskr.models import get_db_session
from flaskr.models.warranty import Warranty
from flaskr.models.trunk import Trunk
import datetime


bp = Blueprint('health_check', __name__, url_prefix='/health')


@bp.route('/check', methods=('GET',))
def check():
    if request.method == 'GET':
        with get_db_session() as session:
            warranty = Warranty(start_date=datetime.date(2018, 8, 8),
                                end_date=datetime.date(2019, 8, 8))
            trunk = Trunk(width=10, height=10, form_factor='ATX')
            session.add(warranty)
            session.add(trunk)
        return 'OK'
