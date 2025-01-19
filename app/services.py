import os
import requests
import pandas as pd
import json

# Diretório de downloads
download_dir = os.path.join(os.getcwd(), 'downloads')

# Garantir que o diretório de downloads exista
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

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
        filename = os.path.join(download_dir, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    except Exception as e:
        print(f'Erro ao baixar o arquivo de {url}: {e}')
        return None

# Função para converter o arquivo CSV em JSON
def convert_csv_to_json(csv_file_path):
    try:
        # Lê o arquivo CSV usando o pandas
        df = pd.read_csv(csv_file_path, delimiter=';', on_bad_lines='skip')
        json_file_path = csv_file_path.replace('.csv', '.json')
        
        # Salva o arquivo JSON
        df.to_json(json_file_path, orient='records', lines=True)
        return json_file_path
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
    csv_file = download_file(url)
    if csv_file:
        json_file = convert_csv_to_json(csv_file)
        if json_file:
            with open(json_file, 'r') as f:
                data = f.read()
            return {
                "statusCode": 200,
                "body": json.dumps({"data": data})
            }
    
    return {
        "statusCode": 500,
        "body": json.dumps({"error": "Erro ao processar o arquivo"})
    }