from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Minecraft', 'Sandbox', 'PC')
    jogo2 = Jogo('The Sims', 'Simulador de vida real', 'PC')
    jogo3 = Jogo('Age of Empires III', 'Estratégia em tempo real', 'PC')
    jogos = [jogo1, jogo2, jogo3]
    return render_template('aprendendo_flask.html', titulo = 'Jogos',lista=jogos)

app.run()