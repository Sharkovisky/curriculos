from app import app, db
from flask import render_template
from app.models.tables import Instituicao
from flask import request

@app.route('/instituicoes')
def listar_instituicoes():
    i = Instituicao.query.all()
    return render_template('listar_instituicoes.html', lista=i)

@app.route('/instituicoes/<instituicao_id>')
def detalhar_instituicoes(instituicao_id):
    i = Instituicao.query.filter_by(id=instituicao_id).first()
    return render_template('detalhar_instituicoes.html', detalhe=i)

@app.route('/instituicoes/nova')
def carregar_formulario():
    return render_template('formulario_instituicoes.html')

@app.route('/instituicoes/inserir', methods=['POST'])
def inserir_instituicao():
    
    #Recebendo os dados
    nome = request.form['nome']
    sigla = request.form['sigla']

    #Cadastrando os dados
    i1 = Instituicao(nome=nome, sigla=sigla)
    db.session.add(i1)
    db.session.commit()

    i = Instituicao.query.all()
    return render_template('listar_instituicoes.html', lista=i)