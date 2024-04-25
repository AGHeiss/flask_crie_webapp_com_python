from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Minecraft', 'Sandbox', 'PC')
jogo2 = Jogo('The Sims', 'Simulador de vida real', 'PC')
jogo3 = Jogo('Age of Empires III', 'Estratégia em tempo real', 'PC')
jogos = [jogo1, jogo2, jogo3]


app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('aprendendo_flask.html', titulo = 'Jogos',lista=jogos)

@app.route('/novo')
def cadastro():
    return render_template('cadastro.html', titulo = 'Novo Jogo')

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    return render_template('aprendendo_flask.html', titulo = 'Jogos', lista=jogos)


app.run(debug=True)