import io
import pandas as pd
from flask import jsonify, Response
import requests

# URLs para cada categoria
urls = {
    "producao": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "processamento": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
    "comercio": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    "importacao": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
    "exportacao": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv"
}

# Função para obter o arquivo CSV e convertê-lo diretamente para JSON sem salvar no servidor
def get_json_for_category(category):
    try:
        # Baixar o arquivo CSV
        url = urls.get(category)
        if not url:
            return jsonify({"message": "Categoria não encontrada"}), 404
        
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta não for 200

        # Converte o CSV em DataFrame usando pandas
        df = pd.read_csv(io.StringIO(response.text), delimiter=';', on_bad_lines='skip')

        # Cria o nome do arquivo JSON com base na categoria
        json_filename = f"{category}_data.json"
        
        # Cria o JSON em memória
        json_data = df.to_json(orient='records', lines=True)

        # Retorna o JSON diretamente na resposta, com cabeçalho para download
        return Response(
            json_data,
            mimetype='application/json',
            headers={"Content-Disposition": f"attachment;filename={json_filename}"}
        )

    except Exception as e:
        return jsonify({"message": f"Erro ao processar arquivo: {str(e)}"}), 500