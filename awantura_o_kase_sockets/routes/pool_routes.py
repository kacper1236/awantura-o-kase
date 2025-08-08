from flask_socketio import emit
from database.Entity.pool import get_pool, reset_pool
from extentions import db

def register_pool_socketio_handlers(socketio):
    @socketio.on('get_pool')
    def handle_get_pool():
        pool_data = get_pool(db)
        if pool_data:
            emit('pool_data', pool_data)
        else:
            emit('error', {'error': 'No pool data found'})

    @socketio.on('reset_pool')
    def handle_reset_pool():
        reset_pool(db)
        emit('pool_reset', {'message': 'Pool reset successfully'}, broadcast=True)
