# controllers/user_controller.py
from flask import render_template, request, redirect, url_for, flash
from models.user import User, db  # ← db viene del modelo

def index():
    users = User.query.all()
    return render_template('index.html', users=users)

def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        if User.query.filter_by(email=email).first():
            flash('Error: Este email ya está registrado.')
            return render_template('create.html')
        
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        flash('Usuario creado con éxito!')
        return redirect(url_for('index'))
    
    return render_template('create.html')

def edit(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        existing = User.query.filter(User.email == email, User.id != user_id).first()
        if existing:
            flash('Error: Este email ya está en uso.')
            return render_template('edit.html', user=user)
        
        user.name = name
        user.email = email
        db.session.commit()
        flash('Usuario actualizado!')
        return redirect(url_for('index'))
    
    return render_template('edit.html', user=user)

def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuario eliminado.')
    return redirect(url_for('index'))