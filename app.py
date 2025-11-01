# app.py
from flask import Flask
from controllers.user_controller import index, create, edit, delete

app = Flask(__name__)

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