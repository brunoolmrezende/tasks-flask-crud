from flask import Flask

# Inicializando a aplicação
app = Flask(__name__)

# Definindo a rota '/hello-world'
@app.route("/hello-world")
def hello_world():
    return "<h1>Hello World!</h1>"

# Definindo a rota '/about'
@app.route("/about")
def about():
    return "<p>Página sobre.</p>"

# Executando a aplicação
if __name__ == "__main__":
    app.run(debug=True)
