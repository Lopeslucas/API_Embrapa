# API Embrapa - Tech Challenge (Fase 1) - Machine Learning Engineering

Esta API foi criada como parte do projeto da Pos_tech - Tech Challenge - Fase 1. Seu objetivo principal é consultar e fornecer dados de diferentes categorias disponibilizadas pela Embrapa, para serem utilizados em um futuro modelo de Machine Learning. A API permite acessar dados das seguintes categorias: Produção, Processamento, Comercialização, Importação e Exportação.

## Objetivo do Projeto

O projeto tem como foco o desenvolvimento de uma API pública que:
- Realiza consultas nos dados do site da Embrapa.
- Informações estruturada através de endpoints.
- Disponibiliza os dados em formato JSON, com suporte a download diretamente pelo navegador.
- Alimenta uma base de dados que será utilizada futuramente para treinamento de modelos de Machine Learning.
- Está preparada para ser escalável, com um plano de deploy que integra a ingestão dos dados até a alimentação de modelos de ML.

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
- **Descrição**: Retorna os dados de comercio em formato JSON.
- **Respostas**:
  - `200 OK`: Dados de Comercio.
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

## Arquitetura e Plano de Deploy

![Arquitetura da API](api-embrapa.png)

Este projeto foi desenvolvido com foco em escalabilidade e facilidade de deploy. A arquitetura foi desenhada para garantir que a ingestão dos dados seja eficiente, e a API será capaz de fornecer informações estruturadas para alimentar modelos de Machine Learning em uma etapa futura.

### Fluxo do Projeto

- **Ingestão de Dados**: A API consulta os dados no site da Embrapa e os disponibiliza nos endpoints em formato JSON.
- **Disponibilidade Dinâmica**: Os dados são convertidos e disponibilizados dinamicamente, com a capacidade de forçar o download do arquivo JSON.
- **Treinamento de Modelos de ML**: Futuramente, esses dados serão utilizados para alimentar modelos de Machine Learning, com o objetivo de realizar previsões ou análises avançadas.

### Deploy

A API foi implantada na plataforma Render, que fornece deploy fácil e escalável para aplicações. Após o deploy, a API está disponível publicamente.

**Link para a API em Produção**:
- A API está disponível em: https://api-embrapa-fk6s.onrender.com

**Documentação Interativa da API**:
- A documentação interativa da API está acessível em: https://api-embrapa-fk6s.onrender.com/apidocs/#/

### Escalabilidade

O projeto foi desenvolvido para ser escalável, garantindo que a API consiga atender a um grande volume de requisições, especialmente com a ingestão de dados e a utilização futura para treinamento de modelos de Machine Learning.

### Contribuições

Contribuições são bem-vindas! Se você deseja colaborar no desenvolvimento deste projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch para suas modificações.
3. Faça as modificações e envie um pull request.

### Licença

Este projeto está licenciado sob a MIT License.