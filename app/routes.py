import requests

import pandas as pd                                  # Adicionado pandas
import joblib                                        # Para carregar o modelo
import io
import os                                            # Para manipulação de caminhos
from flask import jsonify, Response, request 

from app.services import get_json_for_category
from app.models.train_models import preprocess_data  # Importe a função de pré-processamento
from app.database import save_data                   # Importa a função para salvar no banco de dados
from app.services import urls                        # Importa o dicionário de URLs



# Carregar o modelo de Machine Learning
model_path = os.path.join(os.path.dirname(__file__), 'models', 'random_forest_classifier.pkl')
model = joblib.load(model_path)


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
       
    @app.route('/api/importacao/save_to_db', methods=['GET'])
    def save_importacao_to_db():
        """Endpoint para salvar os dados tratados de importação no banco de dados."""
        try:
            # Faz o download do arquivo CSV
            response = requests.get(urls['importacao'], timeout=10)  # Adiciona um timeout para evitar bloqueios
            response.raise_for_status()

            # Converte o CSV em DataFrame usando pandas
            df_final = pd.read_csv(io.StringIO(response.text), delimiter=';', on_bad_lines='skip')

            # Aplica o pré-processamento nos dados
            df_tratado = preprocess_data(df_final)

            # Salva os dados tratados no banco de dados
            save_data(df_tratado, 'importacao')

            return jsonify({"message": "Dados tratados da categoria 'importacao' salvos no banco de dados com sucesso!"})
        except Exception as e:
            return jsonify({'message': f"Erro ao processar e salvar os dados: {str(e)}"}), 500

    @app.route('/api/predict', methods=['POST'])
    def predict():
        try:
            data = request.get_json()  # Recebe os dados no formato JSON
            df_final = pd.DataFrame(data['features'])  # Converte os dados para um DataFrame
            df_tratado = preprocess_data(df_final)  # Aplica o pré-processamento nos dados

            # Selecionar apenas as colunas usadas no treinamento
            colunas_treinamento = ["Ano", "Quantidade (Kg)", "Valor (US$)", "Década"]  # Ajuste conforme necessário
            df_tratado = df_tratado[colunas_treinamento]

            prediction = model.predict(df_tratado)  # Realiza a previsão com o modelo
            return jsonify({'prediction': prediction.tolist()})  # Retorna a previsão
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Retorna o erro em caso de falha
