from flask import jsonify, request
from . import bp
from app import db, InvalidArgumentException


@bp.before_request
def before_request():
    pass


@bp.route('/items', methods=['GET'])
def items():
    body = []
    return jsonify(body), 200
