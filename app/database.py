import psycopg2  # Import necessário para conexão com PostgreSQL
import json      # Import necessário para manipular JSON
from sqlalchemy import create_engine
import pandas as pd



def get_connection():
    return psycopg2.connect(
        dbname="embrapa_data",   # Nome do banco de dados
        user="postgres",         # Usuário do banco
        password="NovaSenha123", # Senha do banco
        host="localhost",        # Host do banco (localhost para local)
        port="5432"              # Porta padrão do PostgreSQL
    )

def save_data(df, categoria):
    """Salva os dados tratados no PostgreSQL."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Cria a tabela dinamicamente, se não existir
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {categoria} (
                id SERIAL PRIMARY KEY,
                dados JSONB NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        # Insere cada linha do DataFrame como JSON
        for _, row in df.iterrows():
            cursor.execute(
                f'''
                INSERT INTO {categoria} (dados) VALUES (%s);
                ''',
                (json.dumps(row.to_dict()),)  # Serializa a linha como JSON
            )
        conn.commit()
        print(f"Dados tratados inseridos com sucesso na tabela {categoria}!")
    except Exception as e:
        print(f"Erro ao salvar dados no banco: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()