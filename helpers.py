import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, PasswordField, validators

class FormularioCadastroUsuario(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    cpf = StringField('CPF', [validators.DataRequired(), validators.Length(min=11)])
    email = EmailField('Email', [validators.DataRequired(), validators.Length(min=1, max=50)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    rua = StringField('Rua', [validators.DataRequired(), validators.Length(min=1, max=50)])
    bairro = StringField('Bairro', [validators.DataRequired(), validators.Length(min=1, max=50)])
    cep = StringField('CEP', [validators.DataRequired(), validators.Length(min=8)])

class FormularioAtualizarPerfil(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    cpf = StringField('CPF', [validators.DataRequired(), validators.Length(min=11)])
    email = EmailField('Email', [validators.DataRequired(), validators.Length(min=1, max=50)])
    rua = StringField('Rua', [validators.DataRequired(), validators.Length(min=1, max=50)])
    bairro = StringField('Bairro', [validators.DataRequired(), validators.Length(min=1, max=50)])
    cep = StringField('CEP', [validators.DataRequired(), validators.Length(min=8)])

class FormularioLogin(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Length(min=1, max=50)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])