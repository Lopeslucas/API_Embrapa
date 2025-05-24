import io
import pandas as pd
from flask import jsonify, Response
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
        # Verifica se a categoria existe no dicionário de URLs
        url = urls.get(category)
        if not url:
            return jsonify({"message": "Categoria não encontrada"}), 404
        
        # Faz o download do arquivo CSV
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a resposta não for 200

        # Converte o CSV em DataFrame usando pandas
        df = pd.read_csv(io.StringIO(response.text), delimiter=';', on_bad_lines='skip')

        # Aplica o pré-processamento nos dados
        df_final = preprocess_data(df)

        # Salva os dados tratados no banco de dados
        save_data(category, df_final)
        
        # Cria o nome do arquivo JSON com base na categoria
        json_filename = f"{category}_data.json"

        # Converte o DataFrame tratado para JSON
        json_data = df_final.to_json(orient='records', lines=True)

        # Retorna o JSON diretamente na resposta, com cabeçalho para download
        json_filename = f"{category}_data.json"
        return Response(
            json_data,
            mimetype='application/json',
            headers={"Content-Disposition": f"attachment;filename={json_filename}"}
        )

        return jsonify({"message": f"Dados tratados da categoria '{category}' salvos no banco de dados com sucesso!"})
    except Exception as e:
        return jsonify({"message": f"Erro ao processar e salvar os dados: {str(e)}"}), 500
    
