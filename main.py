from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrybt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

from cliente_view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)