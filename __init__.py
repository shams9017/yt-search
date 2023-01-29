from flask import Flask
from product_routes import product_route

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(product_route)

    return app