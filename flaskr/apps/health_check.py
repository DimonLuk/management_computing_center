from flask import Blueprint, request
bp = Blueprint('health_check', __name__, url_prefix='/health')


@bp.route('/check', methods=('GET',))
def check():
    if request.method == 'GET':
        return 'OK'
