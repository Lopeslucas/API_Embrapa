from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(message="Hello, World!")

# Vercel espera que a variável 'app' seja exportada diretamente.
if __name__ == "__main__":
    app.run()

# Para que a Vercel consiga usar a função corretamente, exportamos 'app' aqui.
# Vercel busca essa variável para executar o servidor no ambiente serverless.
handler = app
