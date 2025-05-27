import requests

import pandas as pd
import pickle  # Para carregar o modelo
import io
import os
from flask import jsonify, Response, request

from app.services import get_json_for_category
from app.models.train_models import preprocess_data
from app.database import save_data
from app.services import urls

# Caminho para o modelo de Machine Learning
model_path = os.path.join(os.path.dirname(__file__), 'models', 'random_forest_classifier.pkl')

# Carregar o modelo usando pickle
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

def init_routes(app):
    @app.route('/api/producao', methods=['GET'])
    def producao():
        """Endpoint para dados de Produção"""
        print("Rota /api/producao registrada!")  # Debug
        return get_json_for_category('producao')

    @app.route('/api/processamento', methods=['GET'])
    def processamento():
        """Endpoint para dados de Processamento"""
        print("Rota /api/processamento registrada!")  # Debug
        return get_json_for_category('processamento')

    @app.route('/api/comercio', methods=['GET'])
    def comercio():
        """Endpoint para dados de comercio"""
        print("Rota /api/comercio registrada!")  # Debug
        return get_json_for_category('comercio')

    @app.route('/api/importacao', methods=['GET'])
    def importacao():
        """Endpoint para dados de Importação"""
        print("Rota /api/importacao registrada!")  # Debug
        return get_json_for_category('importacao')

    @app.route('/api/exportacao', methods=['GET'])
    def exportacao():
        """Endpoint para dados de Exportação"""
        print("Rota /api/exportacao registrada!")  # Debug
        return get_json_for_category('exportacao')
       
    @app.route('/api/importacao/save_to_db', methods=['GET'])
    def save_importacao_to_db():
        """
        Salva os dados tratados de importação no banco de dados.
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