from flask import Blueprint, render_template, request, redirect, url_for
from airbnb_lab2.app.models.entities import Booking
from airbnb_lab2.app.config.db import SessionLocal

booking_bp = Blueprint('booking', __name__, template_folder='../templates')
session = SessionLocal()

@booking_bp.route('/bookings')
def bookings():
    bookings_list = session.query(Booking).all()
    return render_template('bookings.html', bookings=bookings_list)

@booking_bp.route('/add_booking', methods=['POST'])
def add_booking():
    data = request.form
    b = Booking(user_id=int(data['user_id']), housing_id=int(data['housing_id']), status=data['status'])
    session.add(b)
    session.commit()
    return redirect(url_for('booking.bookings'))

@booking_bp.route('/delete_booking/<int:id>')
def delete_booking(id):
    b = session.get(Booking, id)
    if b:
        session.delete(b)
        session.commit()
    return redirect(url_for('booking.bookings'))

@booking_bp.route('/edit_booking/<int:id>', methods=['POST'])
def edit_booking(id):
    b = session.get(Booking, id)
    data = request.form
    b.user_id = int(data['user_id'])
    b.housing_id = int(data['housing_id'])
    b.status = data['status']
    session.commit()
    return redirect(url_for('booking.bookings'))