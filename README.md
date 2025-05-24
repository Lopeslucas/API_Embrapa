# API Embrapa - Tech Challenge (Fase 3) - Machine Learning Engineering

Esta API foi criada como parte do projeto da Pos_tech - Tech Challenge - Fase 1 e reutilizada na fase 3. Seu objetivo principal é consultar e fornecer dados de diferentes categorias disponibilizadas pela Embrapa, para serem utilizados em um modelo de Machine Learning. E disponilizada junto de um dashboard interativo com as predições de novos dados que podem ser inputados.

## Objetivo do Projeto

O projeto tem como foco o desenvolvimento de uma API pública que:
- Realiza consultas nos dados do site da Embrapa.
- Estrutura as informações através de endpoints.
- Disponibiliza os dados em formato JSON, com suporte a download diretamente pelo navegador.
- Permite a visualização e análise de dados por meio de um dashboard interativo.
- Integra um modelo de Machine Learning para realizar predições com base nos dados fornecidos.

Além disso, a API está preparada para ser escalável, com um plano de deploy que integra a ingestão dos dados até a alimentação de modelos de ML.

## Funcionalidades da API

A API possui os seguintes endpoints, que permitem consultar dados específicos de diferentes áreas:

### `/api/producao`
- **Descrição**: Retorna os dados de produção em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Produção.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/processamento`
- **Descrição**: Retorna os dados de processamento em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Processamento.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/comercio`
- **Descrição**: Retorna os dados de comércio em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Comércio.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/importacao`
- **Descrição**: Retorna os dados de importação em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Importação.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/exportacao`
- **Descrição**: Retorna os dados de exportação em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Exportação.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

# API Embrapa - Tech Challenge (Fase 1) - Machine Learning Engineering

Esta API foi criada como parte do projeto da Pos_tech - Tech Challenge - Fase 1. Seu objetivo principal é consultar e fornecer dados de diferentes categorias disponibilizadas pela Embrapa, para serem utilizados em um futuro modelo de Machine Learning. A API permite acessar dados das seguintes categorias: Produção, Processamento, Comercialização, Importação e Exportação.

## Objetivo do Projeto

O projeto tem como foco o desenvolvimento de uma API pública que:
- Realiza consultas nos dados do site da Embrapa.
- Estrutura as informações através de endpoints.
- Disponibiliza os dados em formato JSON, com suporte a download diretamente pelo navegador.
- Permite a visualização e análise de dados por meio de um dashboard interativo.
- Integra um modelo de Machine Learning para realizar predições com base nos dados fornecidos.

Além disso, a API está preparada para ser escalável, com um plano de deploy que integra a ingestão dos dados até a alimentação de modelos de ML.

## Funcionalidades da API

A API possui os seguintes endpoints, que permitem consultar dados específicos de diferentes áreas:

### `/api/producao`
- **Descrição**: Retorna os dados de produção em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Produção.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/processamento`
- **Descrição**: Retorna os dados de processamento em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Processamento.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/comercio`
- **Descrição**: Retorna os dados de comércio em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Comércio.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/importacao`
- **Descrição**: Retorna os dados de importação em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Importação.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

### `/api/exportacao`
- **Descrição**: Retorna os dados de exportação em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Exportação.
  - `404 Not Found`: Categoria não encontrada.
  - `500 Internal Server Error`: Erro ao processar o arquivo.

## Dashboard Interativo

A API agora inclui um dashboard interativo desenvolvido com Dash, que permite a visualização e análise dos dados de importação e exportação. O dashboard está disponível na rota `/dashboard/`.

### Funcionalidades do Dashboard:
- **Gráfico de Barras**: Exibe os países com maior quantidade de importação, com a possibilidade de filtrar por continente.
- **Gráfico de Linha**: Mostra a tendência de importação por década para os 10 países com maior valor de importação.
- **Predição**: Permite realizar predições com base em um modelo de Machine Learning, utilizando os seguintes campos:
  - Ano
  - Quantidade (Kg)
  - Valor (US$)
  - Década

### Como Acessar o Dashboard:
Após iniciar o servidor, o dashboard estará disponível em:

Adicionar URL AQUI


## Como Rodar o Projeto

### Passo 1: Clonar o Repositório
Clone o repositório do projeto para sua máquina local:

```bash
git clone <URL>
cd api_embrapa
```

### Passo 2: Instalar Dependências
Instale as dependências do projeto utilizando o pip:

```bash
pip install -r requirements.txt
```

### Passo 3: Executar a Aplicação
Execute o arquivo principal do projeto:

```bash
python run.py
```

Após rodar o projeto, a API estará disponível localmente e você poderá acessar os endpoints definidos.

### Fluxo do Projeto

- **Ingestão de Dados**: A API consulta os dados no site da Embrapa e os disponibiliza nos endpoints em formato JSON.
- **Disponibilidade Dinâmica**: Os dados são convertidos e disponibilizados dinamicamente, com a capacidade de forçar o download do arquivo JSON.
- **Dashboard interativo**: Dahsboard contendo graficos interativos para analise dos dados
- **Treinamento de Modelos de ML**: Campos para inpurtar novos dados e obter a predição do modelo de machine learning

### Deploy

A API foi implantada na plataforma Render, que fornece deploy fácil e escalável para aplicações. Após o deploy, a API está disponível publicamente.

**Link para a API em Produção**:
- A API está disponível em: https://api-embrapa-fk6s.onrender.com

**Documentação Interativa da API**:
- A documentação interativa da API está acessível em: https://api-embrapa-fk6s.onrender.com/apidocs/#/

### Contribuições

Contribuições são bem-vindas! Se você deseja colaborar no desenvolvimento deste projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch para suas modificações.
3. Faça as modificações e envie um pull request.

### Licença

Este projeto está licenciado sob a MIT License.