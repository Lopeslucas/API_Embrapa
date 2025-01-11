# API Embrapa

Esta API serve para baixar e converter arquivos CSV disponibilizados pela Embrapa.

## Endpoints

### `/api/producao`
- Descrição: Retorna os dados de produção em formato JSON.
- Respostas:
    - 200: Dados de Produção.
    - 404: Categoria não encontrada.
    - 500: Erro ao processar o arquivo.

### `/api/processamento`
- Descrição: Retorna os dados de processamento em formato JSON.
- Respostas:
    - 200: Dados de Processamento.
    - 404: Categoria não encontrada.
    - 500: Erro ao processar o arquivo.

### `/api/comercializacao`
- Descrição: Retorna os dados de comercialização em formato JSON.
- Respostas:
    - 200: Dados de Comercialização.
    - 404: Categoria não encontrada.
    - 500: Erro ao processar o arquivo.

### `/api/importacao`
- Descrição: Retorna os dados de importação em formato JSON.
- Respostas:
    - 200: Dados de Importação.
    - 404: Categoria não encontrada.
    - 500: Erro ao processar o arquivo.

### `/api/exportacao`
- Descrição: Retorna os dados de exportação em formato JSON.
- Respostas:
    - 200: Dados de Exportação.
    - 404: Categoria não encontrada.
    - 500: Erro ao processar o arquivo.

## Como rodar o projeto

1. Clone o repositório:
    ```bash
    git clone <URL>
    cd api_embrapa
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```bash
    python run.py
    ```

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
