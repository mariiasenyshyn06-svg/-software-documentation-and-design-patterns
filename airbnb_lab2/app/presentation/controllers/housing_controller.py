from flask import Blueprint, render_template, request, redirect, url_for
from airbnb_lab2.app.models.entities import Housing
from airbnb_lab2.app.config.db import SessionLocal

housing_bp = Blueprint('housing', __name__, template_folder='../templates')
session = SessionLocal()

@housing_bp.route('/housing')
def housing():
    housing_list = session.query(Housing).all()
    return render_template('housing.html', housing=housing_list)

@housing_bp.route('/add_housing', methods=['POST'])
def add_housing():
    data = request.form
    h = Housing(address=data['address'], price=float(data['price']), rooms=int(data['rooms']))
    session.add(h)
    session.commit()
    return redirect(url_for('housing.housing'))

@housing_bp.route('/delete_housing/<int:id>')
def delete_housing(id):
    h = session.get(Housing, id)
    if h:
        session.delete(h)
        session.commit()
    return redirect(url_for('housing.housing'))

@housing_bp.route('/edit_housing/<int:id>', methods=['POST'])
def edit_housing(id):
    h = session.get(Housing, id)
    data = request.form
    h.address = data['address']
    h.price = float(data['price'])
    h.rooms = int(data['rooms'])
    session.commit()
    return redirect(url_for('housing.housing'))