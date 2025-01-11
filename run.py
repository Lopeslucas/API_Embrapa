# run.py
from app import create_app  # Importando a função para criar o app

app = create_app()  # Criando a instância do app

if __name__ == "__main__":
    app.run(debug=True)

