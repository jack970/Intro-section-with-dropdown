from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():return render_template("home.html")

@app.route("/contatos")
def contatos():return render_template("contatos.html")

@app.route("/usuario/<usuario>")
def usuario(usuario): return render_template("usuario.html", usuario=usuario)

@app.route("/login")
def login(): return render_template("login.html")

@app.route("/cadastro")
def cadastro(): return render_template("cadastro.html")

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f'post {post_id}'

