from flask import jsonify, Response
from app.services import get_json_for_category

def init_routes(app):
    @app.route('/api/producao', methods=['GET'])
    def producao():
        """Endpoint para dados de Produção
        --- 
        responses:
            200:
                description: Dados de Produção
            404:
                description: Categoria não encontrada
            500:
                description: Erro ao processar arquivo
        """
        print("Rota /api/producao registrada!")  # Debug
        return get_json_for_category('producao')

    @app.route('/api/processamento', methods=['GET'])
    def processamento():
        """Endpoint para dados de Processamento
        --- 
        responses:
            200:
                description: Dados de Processamento
            404:
                description: Categoria não encontrada
            500:
                description: Erro ao processar arquivo
        """
        print("Rota /api/processamento registrada!")  # Debug
        return get_json_for_category('processamento')

    @app.route('/api/comercio', methods=['GET'])
    def comercio():
        """Endpoint para dados de comercio
        --- 
        responses:
            200:
                description: Dados de comercio
            404:
                description: Categoria não encontrada
            500:
                description: Erro ao processar arquivo
        """
        print("Rota /api/comercio registrada!")  # Debug
        return get_json_for_category('comercio')

    @app.route('/api/importacao', methods=['GET'])
    def importacao():
        """Endpoint para dados de Importação
        --- 
        responses:
            200:
                description: Dados de Importação
            404:
                description: Categoria não encontrada
            500:
                description: Erro ao processar arquivo
        """
        print("Rota /api/importacao registrada!")  # Debug
        return get_json_for_category('importacao')

    @app.route('/api/exportacao', methods=['GET'])
    def exportacao():
        """Endpoint para dados de Exportação
        --- 
        responses:
            200:
                description: Dados de Exportação
            404:
                description: Categoria não encontrada
            500:
                description: Erro ao processar arquivo
        """
        print("Rota /api/exportacao registrada!")  # Debug
        return get_json_for_category('exportacao')
