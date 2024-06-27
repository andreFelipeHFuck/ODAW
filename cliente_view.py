from main import app, db
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import generate_password_hash, check_password_hash
from models import Cliente
from helpers import FormularioCadastroUsuario, FormularioLogin, FormularioAtualizarPerfil

@app.route('/secao')
def secao():
    return render_template('secao.html')

@app.route('/login')
def login():
    form = FormularioLogin()
    return render_template('login.html', form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioLogin(request.form)
    cliente = Cliente.query.filter_by(email=form.email.data).first()

    if cliente:
        senha = check_password_hash(cliente.senha, form.senha.data)
        session['logged_in'] = True
        session['id'] = cliente.codCliente
        session['nome'] = cliente.nome

        if senha:
            return redirect(url_for('pagina_perfil', id=cliente.codCliente, cliente=cliente))
        else:
            return redirect(url_for('index'))

    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_in'] = None
    session['id'] = None
    session['nome'] = None

    return redirect(url_for('index'))

@app.route('/cadastrar')
def cadastrar():

    form = FormularioCadastroUsuario()
    return render_template('cadastrar.html', form=form)

@app.route('/cria_cliente', methods=['POST', ])
def cria_cliente():
    form = FormularioCadastroUsuario(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('cadastrar'))
    
    nome = form.nome.data
    cpf = form.cpf.data
    email = form.email.data
    senha = generate_password_hash(form.senha.data).decode('utf-8')
    rua = form.rua.data
    bairro = form.bairro.data
    cep = form.cep.data

    ver_cpf = Cliente.query.filter_by(cpf=cpf).first()
    ver_email = Cliente.query.filter_by(email=email).first()

    if ver_cpf:
        # flash
        return redirect(url_for('index'))
    
    if ver_email:
        # flash
        return redirect(url_for('index'))
    
    novo_cliente = Cliente(
        nome=nome,
        cpf = cpf,
        email = email,
        senha = senha,
        rua = rua,
        bairro = bairro,
        cep = cep,
        tipo = 0
    )

    db.session.add(novo_cliente)
    db.session.commit()

    session['cliente_logado'] = nome

    cliente = Cliente.query.filter_by(email=email, senha=senha).first()

    return redirect(url_for('pagina_perfil', id=cliente.codCliente, cliente=cliente))

@app.route('/perfil/<int:id>')
def pagina_perfil(id):
    if 'cliente_logado' not in session or session['cliente_logado'] == None:
        return redirect(url_for('login'))
    

    cliente = Cliente.query.filter_by(codCliente=id).first()
    return render_template('perfil_usuario.html', cliente=cliente)

@app.route('/editar_perfil/<int:id>')
def editar_perfil(id):
    if 'cliente_logado' not in session or session['cliente_logado'] == None:
        return redirect(url_for('login'))
    
    cliente = Cliente.query.filter_by(codCliente=id).first()

    form = FormularioAtualizarPerfil()
    form.nome.data = cliente.nome
    form.cpf.data = cliente.cpf
    form.email.data = cliente.email
    form.rua.data = cliente.rua
    form.bairro.data = cliente.bairro
    form.cep.data = cliente.cep
    
    return render_template('editar_usuario.html', form=form)

@app.route('/atualizar', methods=['POST', ])
def atualizar_cliente():
    form = FormularioAtualizarPerfil(request.form)

    if form.validate_on_submit():

        cliente = Cliente.query.filter_by(codCliente=session.get('id')).first()
        cliente.nome = form.nome.data
        cliente.cpf = form.cpf.data
        cliente.email = form.email.data
        cliente.rua = form.rua.data
        cliente.bairro = form.bairro.data
        cliente.cep = form.cep.data
        cliente.tipo = 0

        db.session.add(cliente)
        db.session.commit()

        return redirect(url_for('pagina_perfil', id=cliente.codCliente, cliente=cliente))

    return redirect(url_for('index'))


