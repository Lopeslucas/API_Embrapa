import os
import requests
import pandas as pd
from flask import jsonify

download_dir = os.path.join(os.getcwd(), 'downloads')

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

urls = {
    "producao": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "processamento": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
    "comercializacao": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    "importacao": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
    "exportacao": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
}

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.join(download_dir, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    except Exception as e:
        print(f'Erro ao baixar o arquivo de {url}: {e}')
        return None

def convert_csv_to_json(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path, delimiter=';', on_bad_lines='skip')
        json_file_path = csv_file_path.replace('.csv', '.json')
        df.to_json(json_file_path, orient='records', lines=True)
        return json_file_path
    except Exception as e:
        print(f'Erro ao converter o CSV para JSON: {e}')
        return None

def get_data_for_category(category):
    if category not in urls:
        return jsonify({"error": "Categoria não encontrada"}), 404

    url = urls[category]
    csv_file = download_file(url)
    if csv_file:
        json_file = convert_csv_to_json(csv_file)
        if json_file:
            with open(json_file, 'r') as f:
                data = f.read()
            return jsonify({"data": data}), 200
    return jsonify({"error": "Erro ao processar o arquivo"}), 500
