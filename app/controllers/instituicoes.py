from app import app
from flask import render_template
from app.models.tables import Instituicao

@app.route('/instituicoes')
def listar_instituicoes():
    i = Instituicao.query.all()
    return render_template('listar_instituicoes.html', lista=i)