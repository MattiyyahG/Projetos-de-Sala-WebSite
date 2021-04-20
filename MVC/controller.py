from flask import Flask
from flask import render_template, request
import modelo

app = Flask(__name__)

@app.route("/")
def ola():
    return render_template("visao.html")

@app.route("/cadastro", methods = ["POST", "GET"])
def cadastro():
    #pegar os dados da visao
    #mandar os dados para o modelo
    user = ""
    senha = ""

    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        if user == "" or senha == "":
            return "<h1>Por favor cadastre usuario e senha</h1>"
        else:
            pessoa = modelo.Aluno(user,senha)
            pessoa.salva()
            return "<h1>Registro salvo com sucesso</h1> <meta http-equiv='Refresh' content= '2; url=https://www.w3schools.com/codegame/index.html'/>"

app.run() 