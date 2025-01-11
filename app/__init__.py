from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)
    return app