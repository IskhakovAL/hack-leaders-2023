from flask import Blueprint

from app.controllers.responses_controller import resp_ok

node = Blueprint('node', __name__)


@node.get('/api/version')
def get_version():
    return resp_ok('Server is working! Version 1.0.0')

