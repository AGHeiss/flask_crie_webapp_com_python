from flask import Flask, render_template, request, redirect, session, flash

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
app.secret_key = 'ABCD'
@app.route('/home')
def index():
    return render_template('aprendendo_flask.html', titulo = 'Jogos',lista=jogos)

@app.route('/novo')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')

    return render_template('cadastro.html', titulo = 'Novo Jogo')

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    return redirect('/home')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    senha = request.form['senha']
    if 'alohomora' == senha:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logado com sucesso!')
        return redirect('/home')
    else:
        flash('Senha incorreta!')
        return redirect('/login')

@app.route('/deslogar')
def deslogar():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso')
    return redirect('/login')


app.run(debug=True)