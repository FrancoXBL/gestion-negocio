from flask import Flask
from routes.client import clients
from routes.articles import articles
from routes.ventas import ventas
from routes.stockcontrol import stock

app = Flask(__name__)

app.register_blueprint(clients)
app.register_blueprint(articles)
app.register_blueprint(ventas)
app.register_blueprint(stock)
