from uuid import uuid4
from flask import Blueprint, jsonify


BP = Blueprint('uuid', __name__)


@BP.route('/new', methods=['GET'])
def get_blob():
    return jsonify({"id": str(uuid4())})
