from fastapi import APIRouter

node = APIRouter(
    prefix='/api/server',
    tags=['server']
)


@node.get('/version')
def api_server_version():
    return {
        'server': 'Working',
        'status': '1.0.0'
    }
