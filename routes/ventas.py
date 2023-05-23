from flask import Blueprint, render_template

ventas = Blueprint('ventas', __name__)

@ventas.route('/new-venta')
def newVenta():
    return render_template('ventas/new-ventas.html')