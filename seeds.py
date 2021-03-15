from app import db
from app.models.tables import Usuario, Instituicao, Curso
import bcrypt


#Criando usuários
senha_plana = 'Suporte99' 
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
u1 = Usuario(nome='Marco', email='marco@gmail.com', senha=senha_encriptada)
db.session.add(u1)
db.session.commit()

#Criando Instituições
i1 = Instituicao(nome='Instituto Federal de Rondônia', sigla='IFRO')
i2 = Instituicao(nome='Alpha Software')
db.session.add(i1)
db.session.add(i2)
db.session.commit()

#Criando Cursos
iIFRO = Instituicao.query.filter_by(sigla='IFRO').first()
c1 = Curso(nome='Análise e Desenvolvimento de Sistemas', instituicao_id=iIFRO.id)
c2 = Curso(nome='Arquitetura', instituicao_id=iIFRO.id)
db.session.add(c1)
db.session.add(c2)
db.session.commit()