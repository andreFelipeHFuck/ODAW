from main import db

class Cliente(db.Model):
    codCliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name

# class Estado(db.Model):
#     codEstado = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(100))

#     def __repr__(self):
#         return '<Name %r' % self.name

# class Cidade(db.Model):
#     codCidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(100), nullable=False)
#     populacao = db.Column(db.Integer, nullable=False)
#     descricao = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return '<Name %r' % self.name

# class Hotel(db.Model):
#     codHotel = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(50), nullable=False)
#     numQuartos = db.Column(db.Integer, nullable=False)
#     categoria = db.Column(db.Integer, nullable=False)
#     rua = db.Column(db.String(50), nullable=False)
#     bairro = db.Column(db.String(50), nullable=False)
#     cep = db.Column(db.String(8), nullable=False)
#     cidade_codCidade = db.Column(db.Integer, db.ForeignKey('cidade.codCidade'))

#     def __repr__(self):
#         return '<Name %r' % self.name


# class Pacote(db.Model):
#     codPacote = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     preco = db.Column(db.Float, nullable=False)
#     dataInicio = db.Column(db.DateTime, nullable=False)
#     dataFim = db.Column(db.DateTime, nullable=False)
#     cidade_codCidade = db.Column(db.Integer, db.ForeignKey('cidade.codCidade'))
#     hotel_codHotel = db.Column(db.Integer, db.ForeignKey('hotel.codHotel'))
#     cidade_codCidade = db.Column(db.Integer, db.ForeignKey('cidade.codCidade'))

#     def __repr__(self):
#         return '<Name %r' % self.name

# class PontoTuristico(db.Model):
#     codPontoTuristico = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(100), nullable=False)
#     descricao = db.Column(db.Text, nullable=False)
#     rua = db.Column(db.String(50), nullable=False)
#     bairro = db.Column(db.String(50), nullable=False)
#     cep = db.Column(db.String(8), nullable=False)
#     cidade_codCidade = db.Column(db.Integer, db.ForeignKey('cidade.codCidade'))

#     def __repr__(self):
#         return '<Name %r' % self.name

# class Restaurante(db.Model):
#     codRestaurante = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(50), nullable=False)
#     categoria = db.Column(db.Integer, nullable=False)
#     descricao = db.Column(db.Text, nullable=False)
#     precoMedio = db.Column(db.Float, nullable=False)
#     rua = db.Column(db.String(50), nullable=False)
#     bairro = db.Column(db.String(50), nullable=False)
#     cep = db.Column(db.String(8), nullable=False)
#     cidade_codCidade = db.Column(db.Integer, db.ForeignKey('cidade.codCidade'))

#     def __repr__(self):
#         return '<Name %r' % self.name

# class Cliente_has_Pacote(db.Model):
#     cliente_codCliente = db.Column(db.Integer, db.ForeignKey('cliente.codCliente'))
#     pacote_codPacote = db.Column(db.Integer, db.ForeignKey('pacote.codPacote'))

#     def __repr__(self):
#         return '<Name %r' % self.name

# class Pacotes_has_pontoTuristico(db.Model):
#     pacote_codPacote = db.Column(db.Integer, db.ForeignKey('pacote.codPacote'))
#     pontoTuristico_codPontoTuristico = db.Column(db.Integer, db.ForeignKey('pontoTuristico.codPontoTuristico'))

#     def __repr__(self):
#         return '<Name %r' % self.name

