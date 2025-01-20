import os
from app import create_app
from waitress import serve  # Importa o Waitress para rodar em produção no Windows

app = create_app()

# Log para depuração
print("Aplicação Flask inicializada com sucesso!")

if __name__ == "__main__":
    # Usa o Waitress em vez do app.run() do Flask
    print("Executando Flask no modo local (Windows)...")
    port = int(os.environ.get("PORT", 5000))  # Vercel define a porta via variável de ambiente
    serve(app, host="0.0.0.0", port=port)  # Usa o 0.0.0.0 para garantir que o app seja acessível de qualquer lugar