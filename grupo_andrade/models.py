from datetime import datetime
from grupo_andrade import db, login_manager, app
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='padrao.png')
    password = db.Column(db.String(80), nullable=False)
    placas = db.relationship('Placa', backref='author', lazy=True)

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': str(self.id)})

    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    def __repr__(self):
        return f" User(username={self.username}, email={self.email})"



class Placa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(80), unique=False, nullable=False)
    renavan = db.Column(db.String(120), unique=False, nullable=False)
    endereco_placa = db.Column(db.String(120), unique=False, nullable=False)
    crlv = db.Column(db.String(80), nullable=False)
    date_create = db.Column(db.DateTime, nullable=False, default=datetime.now)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    received = db.Column(db.Boolean, default=False)
    received_at = db.Column(db.DateTime, nullable=True, default=datetime.now)  # Hora da confirmação
        
    def __repr__(self):
        return f"Placa(placa={self.placa})"
    

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(255), nullable=True, default='Nenhum Endereço')  # Campo de endereço
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # FK para User

    def __repr__(self):
        return f"Endereco(endereco={self.endereco})"



class Pagamento(db.Model):
    __tablename__ = 'pagamento'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)  # ID do pagamento
    id_pagamento = db.Column(db.String(255), unique=False, nullable=False)  # ID retornado pela API do Mercado Pago
    status_pagamento = db.Column(db.String(50), nullable=False)  # Status do pagamento (ex: 'aprovado', 'recusado')
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ID do usuário associado
    date_pagamento = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f'<Pagamento {self.id} - {self.status_pagamento}>'