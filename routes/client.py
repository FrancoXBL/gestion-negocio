from flask import Blueprint, render_template

clients = Blueprint('clients', __name__)

@clients.route("/")
def base():
    return render_template('clients/client.html')


@clients.route('/new-client')
def add_client():
    return render_template('clients/new-client.html')

@clients.route('/edit-client')
def edit_client():
    return render_template('clients/edit-client.html')
