# controllers/user_controller.py
from models.user import User
from flask import render_template, request, redirect, url_for

def index():
    users = User.get_all()
    return render_template('index.html', users=users)

def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        User.create(name, email)
        return redirect(url_for('index'))
    return render_template('create.html')

def edit(user_id):
    user = User.get_by_id(user_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        User.update(user_id, name, email)
        return redirect(url_for('index'))
    return render_template('edit.html', user=user)

def delete(user_id):
    User.delete(user_id)
    return redirect(url_for('index'))