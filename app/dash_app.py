from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
import os
import pickle  # Use pickle ao invés de joblib

def init_dashboard(server):
    """Inicializa o Dash e o integra com o servidor Flask."""
    # Caminho relativo para o CSV
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'importacao_dados_transformados.csv')
    df = pd.read_csv(csv_path, delimiter=',')

    # Caminho relativo para o modelo
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'random_forest_classifier.pkl')

    # Carregar o modelo usando pickle
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Prepare os dados para o gráfico de linha
    top_10_paises = df.groupby("País")["Valor (US$)"].sum().sort_values(ascending=False).head(10).index
    dados_top_10_decadas = df[df["País"].isin(top_10_paises)]

    # Inicialize o Dash
    dash_app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

    # Layout do Dash
    dash_app.layout = html.Div([
        html.H1("Dashboard de Importação e Predição"),
        
        # Dropdown para selecionar o continente
        html.Label("Filtrar por Continente:"),
        dcc.Dropdown(
            id='continente-dropdown',
            options=[{'label': cont, 'value': cont} for cont in df['Continente'].unique()],
            value=None,  # Valor inicial (nenhum filtro)
            placeholder="Selecione um continente",
            clearable=True
        ),
        
        # Gráfico interativo de barras
        dcc.Graph(id='grafico-importacao', style={'height': '700px'}),  # Aumenta o eixo vertical

        html.Hr(),

        # Gráfico de linha para tendências de importação por década
        html.H2("Tendência de Importação por Década (Top 10 Países)"),
        dcc.Graph(
            id='grafico-linha-decadas',
            figure=px.line(
                dados_top_10_decadas,
                x="Década",
                y="Valor (US$)",
                color="País",
                markers=True,
                title="Tendência de Importação por Década (Valor em US$) - Top 10 Países"
            ).update_layout(height=500)  # Ajusta a altura do gráfico
        ),

        html.Hr(),

        # Formulário para predição
        html.H2("Predição"),
        html.Label("Ano:"),
        dcc.Input(id='input-ano', type='number', placeholder='Digite o ano', style={'margin-right': '10px'}),
        html.Label("Quantidade (Kg):"),
        dcc.Input(id='input-quantidade', type='number', placeholder='Digite a quantidade', style={'margin-right': '10px'}),
        html.Label("Valor (US$):"),
        dcc.Input(id='input-valor', type='number', placeholder='Digite o valor', style={'margin-right': '10px'}),
        html.Label("Década:"),
        dcc.Input(id='input-decada', type='number', placeholder='Digite a década', style={'margin-right': '10px'}),
        html.Button('Prever', id='botao-prever', n_clicks=0),

        # Resultado da predição
        html.Div(id='resultado-predicao', style={'margin-top': '20px', 'font-weight': 'bold'})
    ])

    # Callback para atualizar o gráfico com base no filtro
    @dash_app.callback(
        Output('grafico-importacao', 'figure'),
        [Input('continente-dropdown', 'value')]
    )
    def atualizar_grafico(continente):
        # Filtra os dados com base no continente selecionado
        if continente:
            df_filtrado = df[df['Continente'] == continente]
        else:
            df_filtrado = df

        # Ordena os dados do maior para o menor com base na coluna 'Quantidade (Kg)'
        df_filtrado = df_filtrado.sort_values(by='Quantidade (Kg)', ascending=False)

        # Cria o gráfico atualizado
        fig = px.bar(
            df_filtrado,
            x='País',
            y='Quantidade (Kg)',
            color='Continente',
            title=f"Quantidade por País{' - ' + continente if continente else ''}"
        )
        fig.update_layout(height=700)  # Ajusta a altura do gráfico
        return fig

    # Callback para realizar a predição
    @dash_app.callback(
        Output('resultado-predicao', 'children'),
        [Input('botao-prever', 'n_clicks')],
        [State('input-ano', 'value'),
         State('input-quantidade', 'value'),
         State('input-valor', 'value'),
         State('input-decada', 'value')]
    )
    def realizar_predicao(n_clicks, ano, quantidade, valor, decada):
        if n_clicks > 0:
            # Verifica se todos os campos foram preenchidos
            if None in [ano, quantidade, valor, decada]:
                return "Por favor, preencha todos os campos para realizar a predição."

            # Cria o DataFrame com os dados de entrada
            dados = pd.DataFrame([{
                'Ano': ano,
                'Quantidade (Kg)': quantidade,
                'Valor (US$)': valor,
                'Década': decada
            }])

            # Realiza a predição
            predicao = model.predict(dados)
            return f"Resultado da Predição: {predicao[0]}"

        return ""

    return dash_app