import os
from app import create_app
from app.dash_app import init_dashboard


app = create_app()

# Inicializa o Dash
init_dashboard(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))        # A porta será fornecida pelo Render
    app.run(debug=True, host="0.0.0.0", port=port)  # Para testes locais, com Flask

for rule in app.url_map.iter_rules():
    print(rule)