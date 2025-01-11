from flask import jsonify
from app.services import get_data_for_category

def init_routes(app):
    @app.route('/api/producao', methods=['GET'])
    def producao():
        return get_data_for_category('producao')

    @app.route('/api/processamento', methods=['GET'])
    def processamento():
        return get_data_for_category('processamento')

    @app.route('/api/comercializacao', methods=['GET'])
    def comercializacao():
        return get_data_for_category('comercializacao')

    @app.route('/api/importacao', methods=['GET'])
    def importacao():
        return get_data_for_category('importacao')

    @app.route('/api/exportacao', methods=['GET'])
    def exportacao():
        return get_data_for_category('exportacao')
