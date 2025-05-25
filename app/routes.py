import requests

import pandas as pd                                  # Adicionado pandas
import pickle                                        # Para carregar o modelo
import io
import os                                            # Para manipulação de caminhos
from flask import jsonify, Response, request 

from app.services import get_json_for_category
from app.models.train_models import preprocess_data  # Importe a função de pré-processamento
from app.database import save_data                   # Importa a função para salvar no banco de dados
from app.services import urls                        # Importa o dicionário de URLs



# Caminho para o modelo de Machine Learning
model_path = os.path.join(os.path.dirname(__file__), 'models', 'random_forest_classifier.joblib')

# Carregar o modelo usando pickle
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)


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
        """
        Salva os dados tratados de importação no banco de dados.
        ---
        responses:
          200:
            description: Dados tratados da categoria 'importacao' salvos no banco de dados com sucesso!
          500:
            description: Erro ao processar e salvar os dados
        """
        try:
            response = requests.get(urls['importacao'], timeout=10)
            response.raise_for_status()
            df_final = pd.read_csv(io.StringIO(response.text), delimiter=';', on_bad_lines='skip')
            df_tratado = preprocess_data(df_final)
            save_data(df_tratado, 'importacao')
            return jsonify({"message": "Dados tratados da categoria 'importacao' salvos no banco de dados com sucesso!"})
        except Exception as e:
            return jsonify({'message': f"Erro ao processar e salvar os dados: {str(e)}"}), 500

    @app.route('/api/predict', methods=['POST'])
    def predict():
        """
        Realiza predição com o modelo treinado.
        ---
        parameters:
          - in: body
            name: features
            schema:
              type: object
              properties:
                features:
                  type: array
                  items:
                    type: object
            required: true
        responses:
          200:
            description: Predição realizada com sucesso
            schema:
              type: object
              properties:
                prediction:
                  type: array
                  items:
                    type: number
          500:
            description: Erro ao realizar a predição
        """
        try:
            data = request.get_json()
            df_final = pd.DataFrame(data['features'])
            df_tratado = preprocess_data(df_final)
            colunas_treinamento = ["Ano", "Quantidade (Kg)", "Valor (US$)", "Década"]
            df_tratado = df_tratado[colunas_treinamento]
            prediction = model.predict(df_tratado)
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
