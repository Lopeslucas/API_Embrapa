import io
import os
import pandas as pd
from flask import jsonify, Response, request
import requests
from app.database import save_data  # Importa a função para salvar no banco de dados
from app.models.train_models import preprocess_data  # Importa a função de pré-processamento


# URLs para cada categoria
urls = {
    "producao": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "processamento": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
    "comercio": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    "importacao": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
    "exportacao": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
}


def get_json_for_category(category):
    try:
        url = urls.get(category)
        if not url:
            return jsonify({"message": "Categoria não encontrada"}), 404

        response = requests.get(url)
        response.raise_for_status()

        # Salva o CSV bruto em app/data/raw/
        raw_dir = os.path.join("app", "data", "raw")
        os.makedirs(raw_dir, exist_ok=True)
        raw_csv_path = os.path.join(raw_dir, f"{category}.csv")
        # Salva o conteúdo exatamente como recebido
        with open(raw_csv_path, "wb") as f:
            f.write(response.content)

        # Lê o CSV bruto para retornar como JSON
        df = pd.read_csv(io.StringIO(response.text), delimiter=';', on_bad_lines='skip')
        json_data = df.to_json(orient='records', lines=True)
        json_filename = f"{category}_data.json"
        return Response(
            json_data,
            mimetype='application/json',
            headers={"Content-Disposition": f"attachment;filename={json_filename}"}
        )
    except Exception as e:
        return jsonify({"message": f"Erro ao processar e salvar os dados: {str(e)}"}), 500
    
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
        
def predict():
    try:
        data = request.get_json()                   # Recebe os dados no formato JSON
        df_final = pd.DataFrame(data['features'])   # Converte os dados para um DataFrame
        df_tratado = preprocess_data(df_final)      # Aplica o pré-processamento nos dados

        # Selecionar apenas as colunas usadas no treinamento
        colunas_treinamento = ["Ano", "Quantidade (Kg)", "Valor (US$)", "Década"]  # Ajuste conforme necessário
        df_tratado = df_tratado[colunas_treinamento]

        prediction = model.predict(df_tratado)  # Realiza a previsão com o modelo
        return jsonify({'prediction': prediction.tolist()})  # Retorna a previsão
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Retorna o erro em caso de falha
