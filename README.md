# API Embrapa - Tech Challenge (Fase 1) - Machine Learning Engineering

Esta API foi criada como parte do projeto da Pos_tech - Tech Challenge - Fase 1. Seu objetivo principal é consultar e fornecer dados de diferentes categorias disponibilizadas pela Embrapa, para serem utilizados em um futuro modelo de Machine Learning. A API permite acessar dados das seguintes categorias: Produção, Processamento, Comercialização, Importação e Exportação.

## Objetivo do Projeto

O projeto tem como foco o desenvolvimento de uma API pública que:
- Realiza consultas nos dados do site da Embrapa.
- Exponibiliza essas informações de maneira estruturada através de endpoints RESTful.
- Alimenta uma base de dados que será utilizada futuramente para treinamento de modelos de Machine Learning.

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

### `/api/comercializacao`
- **Descrição**: Retorna os dados de comercialização em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Comercialização.
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

## Como Rodar o Projeto

### Passo 1: Clonar o Repositório
Clone o repositório do projeto para sua máquina local:

```bash
git clone <URL>
cd api_embrapa
