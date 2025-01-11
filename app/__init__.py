from flask import Flask
from flasgger import Swagger
from app.routes import init_routes  # Certifique-se de importar a função que registra as rotas

def create_app():
    app = Flask(__name__)

    # Inicializando o Swagger
    swagger = Swagger(app)

    # Registrando as rotas
    init_routes(app)

    return app
