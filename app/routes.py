from flask import jsonify
from app.services.services import get_data_for_category

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
        return get_data_for_category('producao')

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
        return get_data_for_category('processamento')

    @app.route('/api/comercializacao', methods=['GET'])
    def comercializacao():
        """Endpoint para dados de Comercialização
        ---
        responses:
            200:
                description: Dados de Comercialização
            404:
                description: Categoria não encontrada
            500:
                description: Erro ao processar arquivo
        """
        return get_data_for_category('comercializacao')

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
        return get_data_for_category('importacao')

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
        return get_data_for_category('exportacao')
