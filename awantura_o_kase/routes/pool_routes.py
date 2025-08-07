from flask import Blueprint
from database.Entity.pool import get_pool, reset_pool
from extentions import db

pool_bp = Blueprint('pool', __name__)

@pool_bp.route('/get-pool', methods=['GET'])
def pool_route():
    pool_data = get_pool(db)
    if pool_data:
        return pool_data, 200
    return {'error': 'No pool data found'}, 404

@pool_bp.route('/reset-pool', methods=['POST'])
def reset_pool_route():
    reset_pool(db)
    return {'message': 'Pool reset successfully'}, 200

