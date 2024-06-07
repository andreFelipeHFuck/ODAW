from main import app
from flask import Flask, render_template
from models import Cliente

@app.route('/secao')
def secao():
    return render_template('secao.html')
