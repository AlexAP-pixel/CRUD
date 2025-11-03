# app.py
from flask import Flask
from config import Config
from models.user import db as models_db, User  # ← Importa db del modelo
from controllers.user_controller import index, create, edit, delete

app = Flask(__name__) # Configura la app Flask
app.config.from_object(Config) # Carga la configuración
app.config['SQLALCHEMY_DATABASE_URI'] = Config.get_db_uri() # Configura la URI de la base de datos

app.secret_key = 'tu_clave_secreta_super_segura_123'

models_db.init_app(app)  # Inicializa SQLAlchemy con la app

with app.app_context():
    models_db.create_all() # Crea las tablas en la base de datos

# Rutas
@app.route('/')
def home():
    return index()

@app.route('/create', methods=['GET', 'POST'])
def create_route():
    return create()

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_route(user_id):
    return edit(user_id)

@app.route('/delete/<int:user_id>')
def delete_route(user_id):
    return delete(user_id)

if __name__ == '__main__':
    app.run(debug=True)