# controllers/user_controller.py
from flask import render_template, request, redirect, url_for, flash
from models.user import User, db

# Función de inicio
def index():
    users = User.query.all() # Obtiene todos los usuarios
    return render_template('index.html', users=users) # Renderiza la plantilla con los usuarios

# Función para crear un nuevo usuario
def create():
    if request.method == 'POST':
        name = request.form['name'] # Obtenemos el nombre
        email = request.form['email'] # Obtenemos el correo
        
        if User.query.filter_by(email=email).first(): # Verifica si el email ya existe
            flash('Error: Este email ya está registrado.') # Muestra un mensaje de error
            return render_template('create.html') 
        
        user = User(name=name, email=email) # Obtenemos nombre y correo
        db.session.add(user) # Lo agregamos a la sesión
        db.session.commit() # Guardamos en la base de datos
        flash('Usuario creado con éxito!')
        return redirect(url_for('home'))  # CAMBIA 'index' → 'home'
    
    return render_template('create.html')

# Función para editar un usuario existente
def edit(user_id):
    user = User.query.get_or_404(user_id) # Obtiene el usuario por ID o devuelve 404 si no existe
    
    if request.method == 'POST': 
        name = request.form['name'] # Obtenemos el nombre
        email = request.form['email'] # Obtenemos el coreo
        
        existing = User.query.filter(User.email == email, User.id != user_id).first() # 
        if existing:
            flash('Error: Este email ya está en uso.')
            return render_template('edit.html', user=user) # 
        
        user.name = name # Actualiza el nombre
        user.email = email # Actualiza el correo
        db.session.commit() # Guarda los cambios
        flash('Usuario actualizado!')
        return redirect(url_for('home'))  # CAMBIA 'index' → 'home'
    
    return render_template('edit.html', user=user)

# Función para eliminar un usuario
def delete(user_id): 
    user = User.query.get_or_404(user_id) # Obtiene el usuario
    db.session.delete(user)
    db.session.commit()
    flash('Usuario eliminado.')
    return redirect(url_for('home'))  # CAMBIA 'index' → 'home'