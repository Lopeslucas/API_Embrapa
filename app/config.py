import os

class Config:
    # Define o diretório de downloads, que será usado para salvar os arquivos CSV e JSON
    DOWNLOAD_DIR = os.path.join(os.getcwd(), 'data', 'raw')

    # Verifica se o diretório de downloads existe, e cria caso não exista
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)