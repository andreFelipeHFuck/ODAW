from main import app, db
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from models import Cliente, Cidade, Hotel, Pacote, Cliente_has_pacote
from helpers import recupera_imagem, converte_data

@app.route('/destinos')
def destinos():
    principais_pacotes = Pacote.query.filter_by().limit(3).all()


    pacotes = []

    return render_template('destinos.html', principais_pacotes=principais_pacotes)

@app.route('/pacote/<int:id>')
def pagina_pacote(id):
    pacote = Pacote.query.filter_by(codPacote=id).first()
    cidade = Cidade.query.filter_by(codCidade=pacote.cidade_codCidade).first()
    hotel = Hotel.query.filter_by(codHotel=pacote.hotel_codHotel).first()

    if 'logged_in' in session or session['logged_in'] == True:
        cliente_has_pacote = Cliente_has_pacote.query.filter_by(
                                cliente_codCliente=session.get('id'),
                                pacote_codPacote=id
                                ).first()
        
        pacote.dataInicio = converte_data(pacote.dataInicio)
        pacote.dataFim = converte_data(pacote.dataFim)

        if not cliente_has_pacote:

            return render_template(
                    'pacote.html', 
                    pacote=pacote, 
                    cidade=cidade,
                    hotel=hotel,
                    comprado=False)
        
        return render_template(
                    'pacote.html', 
                    pacote=pacote, 
                    cidade=cidade,
                    hotel=hotel,
                    comprado=True)

    pacote.dataInicio = converte_data(pacote.dataInicio)
    pacote.dataFim = converte_data(pacote.dataFim)

    return render_template(
                'pacote.html', 
                pacote=pacote, 
                cidade=cidade,
                hotel=hotel,
                comprado=False)

@app.route('/compra_pacote/<int:id>')
def comprar_pacote(id):
    if 'logged_in' not in session or session['logged_in'] == None:
        return redirect(url_for('login'))
    
    cliente_has_pacote = Cliente_has_pacote.query.filter_by(
            cliente_codCliente=session.get('id'),
            pacote_codPacote=id
        ).first()
    
    print(cliente_has_pacote)
    
    if not cliente_has_pacote:
    
        novo_cliente_has_pacote = Cliente_has_pacote(
            cliente_codCliente = session.get('id'),
            pacote_codPacote = id
        )

        db.session.add(novo_cliente_has_pacote)
        db.session.commit()

        cliente = Cliente.query.filter_by(codCliente=session.get('id')).first()

        return redirect(url_for('pagina_perfil', id=cliente.codCliente, cliente=cliente))
    
    pacote = Pacote.query.filter_by(codPacote=id).first()
    return redirect(url_for('pagina_pacote', id=pacote.codPacote))

@app.route('/remover_compra_pacote/<int:id>')
def remover_pacote(id):
    if 'logged_in' not in session or session['logged_in'] == None:
        return redirect(url_for('login'))
    
    Cliente_has_pacote.query.filter_by(cliente_codCliente=session.get('id'), pacote_codPacote=id).delete()
    db.session.commit()

    cliente = Cliente.query.filter_by(codCliente=session.get('id')).first()

    return redirect(url_for('pagina_perfil', id=cliente.codCliente, cliente=cliente))

@app.route('/pacotes/<codPacote>')
def imagem(codPacote):
    nome_arquivo = recupera_imagem(codPacote)
    return send_from_directory('pacotes', nome_arquivo)