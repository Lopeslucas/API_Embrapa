from app import create_app

app = create_app()

# Adiciona log de depuração para verificar se a criação da aplicação ocorre corretamente
print("Aplicação Flask inicializada com sucesso!")

if __name__ == "__main__":
    # Isso vai garantir que a aplicação seja executada corretamente
    print("Executando Flask no modo local...")
    app.run(debug=True)