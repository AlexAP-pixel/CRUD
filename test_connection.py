# test_connection.py
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.get_db_uri()
db = SQLAlchemy(app)

with app.app_context():
    try:
        result = db.engine.execute("SELECT 1").fetchone()
        print("¡CONEXIÓN EXITOSA! SQL Server responde.")
    except Exception as e:
        print("Error de conexión:", e)