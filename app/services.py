import os
import requests
import pandas as pd
import json
import tempfile

# URLs para cada categoria
urls = {
    "producao": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "processamento": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
    "comercializacao": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    "importacao": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
    "exportacao": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
}

# Função para fazer o download do arquivo CSV
def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta não for 200
        return response.content
    except Exception as e:
        print(f'Erro ao baixar o arquivo de {url}: {e}')
        return None

# Função para converter o arquivo CSV em JSON
def convert_csv_to_json(csv_data):
    try:
        # Converte o CSV em um dataframe pandas diretamente da memória
        from io import StringIO
        df = pd.read_csv(StringIO(csv_data.decode('utf-8')), delimiter=';', on_bad_lines='skip')
        
        # Converte o DataFrame para JSON
        json_data = df.to_json(orient='records', lines=True)
        return json_data
    except Exception as e:
        print(f'Erro ao converter o CSV para JSON: {e}')
        return None

# Função para obter os dados para uma categoria específica
def get_data_for_category(category):
    if category not in urls:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Categoria não encontrada"})
        }

    url = urls[category]
    csv_data = download_file(url)
    if csv_data:
        json_data = convert_csv_to_json(csv_data)
        if json_data:
            return {
                "statusCode": 200,
                "body": json.dumps({"data": json_data})
            }
    
    return {
        "statusCode": 500,
        "body": json.dumps({"error": "Erro ao processar o arquivo"})
    }
