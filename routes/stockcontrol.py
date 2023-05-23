from flask import Blueprint

stock = Blueprint('stock', __name__)

@stock.route('/stock')
def controlStock():
    return 'stock control'