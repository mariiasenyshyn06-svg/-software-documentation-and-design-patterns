from flask import Blueprint, render_template, request, redirect, url_for
from airbnb_lab2.app.models.entities import User
from airbnb_lab2.app.config.db import SessionLocal

user_bp = Blueprint('user', __name__, template_folder='../templates')
session = SessionLocal()

@user_bp.route('/users')
def users():
    users = session.query(User).all()
    return render_template('users.html', users=users)

@user_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.form
    user = User(name=data['name'], email=data['email'], password=data['password'])
    session.add(user)
    session.commit()
    return redirect(url_for('user.users'))

@user_bp.route('/delete_user/<int:id>')
def delete_user(id):
    user = session.get(User, id)
    if user:
        session.delete(user)
        session.commit()
    return redirect(url_for('user.users'))

@user_bp.route('/edit_user/<int:id>', methods=['POST'])
def edit_user(id):
    user = session.get(User, id)
    data = request.form
    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    session.commit()
    return redirect(url_for('user.users'))