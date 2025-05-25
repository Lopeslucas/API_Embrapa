import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import pickle

import pandas as pd
import numpy as np
import os

import os
from joblib import dump  # Substituindo pickle por joblib


def preprocess_data(df):
    """Função para realizar o tratamento de dados."""
    # Renomear as colunas
    colunas = ["Id", "País"] + [
        f"{year}_{suffix}" for year in range(1970, 2025) for suffix in ["Quantidade", "Valor"]
    ]
    df.columns = colunas[:len(df.columns)]

    # Transformar os dados para o formato "long"
    df_long = pd.melt(
        df,
        id_vars=["Id", "País"],
        var_name="Ano_Tipo",
        value_name="Valor"
    )

    # Separar a coluna "Ano_Tipo" em "Ano" e "Tipo"
    df_long[["Ano", "Tipo"]] = df_long["Ano_Tipo"].str.split("_", expand=True)

    # Pivotar os dados
    df_final = df_long.pivot_table(
        index=["Id", "País", "Ano"],
        columns="Tipo",
        values="Valor",
        aggfunc="first"
    ).reset_index()

    # Renomear as colunas
    df_final.columns.name = None
    df_final.rename(columns={"Quantidade": "Quantidade (Kg)", "Valor": "Valor (US$)"}, inplace=True)

    # Remover a coluna "Id"
    df_final.drop(columns=["Id"], inplace=True)

    # Converter "Ano" para int
    df_final["Ano"] = pd.to_numeric(df_final["Ano"], errors="coerce").astype(int)

    # Substituir valores 0.0 por NaN
    df_final.loc[
        (df_final["Quantidade (Kg)"] == 0.0) & (df_final["Valor (US$)"] == 0.0),
        ["Quantidade (Kg)", "Valor (US$)"]
    ] = None

    # Remover valores nulos
    df_final.dropna(subset=["Quantidade (Kg)", "Valor (US$)"], inplace=True)

    # Remover outliers com base no intervalo interquartil (IQR)
    Q1 = df_final["Valor (US$)"].quantile(0.25)
    Q3 = df_final["Valor (US$)"].quantile(0.75)
    IQR = Q3 - Q1
    df_final = df_final[~((df_final["Valor (US$)"] < (Q1 - 1.5 * IQR)) | (df_final["Valor (US$)"] > (Q3 + 1.5 * IQR)))]

    # Aplicar transformação logarítmica
    df_final["Valor (US$)"] = np.log1p(df_final["Valor (US$)"])
    df_final["Quantidade (Kg)"] = np.log1p(df_final["Quantidade (Kg)"])

    # Criar novas features
    df_final["Década"] = (df_final["Ano"] // 10) * 10
    df_final["Ano_Quantidade"] = df_final["Ano"] * df_final["Quantidade (Kg)"]

    # Mapeamento de países para continentes
    pais_para_continente = {
        "Africa do Sul": "África",
        "Alemanha": "Europa",
        "Argélia": "África",
        "Arábia Saudita": "Ásia",
        "Argentina": "América do Sul",
        "Armênia": "Ásia",
        "Austrália": "Oceania",
        "Áustria": "Europa",
        "Bermudas": "América do Norte",
        "Bélgica": "Europa",
        "Bolívia": "América do Sul",
        "Bósnia-Herzegovina": "Europa",
        "Brasil": "América do Sul",
        "Bulgária": "Europa",
        "Canada": "América do Norte",
        "Chile": "América do Sul",
        "China": "Ásia",
        "Coreia do Sul, República": "Ásia",
        "Croácia": "Europa",
        "Cuba": "América do Norte",
        "Emirados Árabes Unidos": "Ásia",
        "Eslovênia": "Europa",
        "Eslováquia": "Europa",
        "Espanha": "Europa",
        "Estados Unidos": "América do Norte",
        "França": "Europa",
        "Geórgia": "Ásia",
        "Geórgia do Sul e Sandwich do Sul, Ilhas": "América do Sul",
        "Grécia": "Europa",
        "Hong Kong": "Ásia",
        "Hungria": "Europa",
        "Indonésia": "Ásia",
        "Irlanda": "Europa",
        "Israel": "Ásia",
        "Itália": "Europa",
        "Japão": "Ásia",
        "Iugoslávia": "Europa",
        "Líbano": "Ásia",
        "Luxemburgo": "Europa",
        "Macedônia": "Europa",
        "Marrocos": "África",
        "México": "América do Norte",
        "Moldávia": "Europa",
        "Montenegro": "Europa",
        "Noruega": "Europa",
        "Nova Zelândia": "Oceania",
        "Países Baixos (Holanda)": "Europa",
        "Panamá": "América do Norte",
        "Peru": "América do Sul",
        "Porto Rico": "América do Norte",
        "Portugal": "Europa",
        "Reino Unido": "Europa",
        "Republica Dominicana": "América do Norte",
        "Romênia": "Europa",
        "Rússia": "Europa",
        "San Marino": "Europa",
        "Sérvia": "Europa",
        "Síria": "Ásia",
        "Suazilândia": "África",
        "Suíça": "Europa",
        "Tcheca, República": "Europa",
        "Tunísia": "África",
        "Turquia": "Ásia",
        "Ucrânia": "Europa",
        "Uruguai": "América do Sul",
        "Não consta na tabela": "Desconhecido",
        "Não declarados": "Desconhecido",
        "Outros": "Desconhecido"
    }
    
    df_final["Continente"] = df_final["País"].map(pais_para_continente)

    # Resetar os índices
    df_final.reset_index(drop=True, inplace=True)

    return df_final





def train_and_save_model(data_path, model_path):
    # Carregar os dados tratados
    df_final = pd.read_csv(data_path)

    # Separar variáveis independentes (X) e dependente (y)
    X = df_final[["Ano", "Quantidade (Kg)", "Valor (US$)", "Década"]]
    y = df_final["Continente"]

    # Balanceamento com SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, 
        test_size=0.2, 
        random_state=42
    )

    # Treinar o modelo
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)

    # Avaliar o modelo
    y_pred = model.predict(X_test)
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

    # Salvar o modelo treinado usando joblib (mais recomendado que pickle)
    dump(model, model_path)
    print(f"Modelo salvo em: {model_path}")

if __name__ == "__main__":
    # Caminhos ajustados para formato multiplataforma
    data_path = os.path.join(
        os.path.dirname(__file__), 
        '..', '..', 
        'data', 'processed', 
        'importacao_dados_transformados.csv'
    )
    
    model_path = os.path.join(
        os.path.dirname(__file__), 
        'random_forest_classifier.joblib'  # Mudando a extensão para .joblib
    )
    
    train_and_save_model(
        data_path=data_path,
        model_path=model_path
    )
    
    