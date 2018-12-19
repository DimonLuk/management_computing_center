from flask import Blueprint
from flaskr.models.warranty import Warranty # NOQA
from flaskr.models.component_meta_info import ComponentMetaInfo # NOQA
from flaskr.models.manufacturer import Manufacturer # NOQA
from flaskr.models.trunk import Trunk # NOQA
from flaskr.models.motherboard import Motherboard # NOQA
from flaskr.models.computer import Computer # NOQA
from flaskr.models.ram import Ram # NOQA
from flaskr.models.processor import Processor # NOQA


bp = Blueprint('_agregator', __name__, url_prefix='/_agregator')


@bp.route('/info', methods=('GET',))
def info():
    message = 'This _agregator is created to fetch all newly created db' +\
        'object so they can be found by migration system'
    return message
