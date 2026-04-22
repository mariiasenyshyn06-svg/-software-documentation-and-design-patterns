from flask import Blueprint, render_template, request, redirect, url_for
from airbnb_lab2.app.models.entities import Payment
from airbnb_lab2.app.config.db import SessionLocal

payment_bp = Blueprint('payment', __name__, template_folder='../templates')
session = SessionLocal()

@payment_bp.route('/payments')
def payments():
    payments_list = session.query(Payment).all()
    return render_template('payments.html', payments=payments_list)

@payment_bp.route('/add_payment', methods=['POST'])
def add_payment():
    data = request.form
    p = Payment(booking_id=int(data['booking_id']), amount=float(data['amount']), status=data['status'])
    session.add(p)
    session.commit()
    return redirect(url_for('payment.payments'))

@payment_bp.route('/delete_payment/<int:id>')
def delete_payment(id):
    p = session.get(Payment, id)
    if p:
        session.delete(p)
        session.commit()
    return redirect(url_for('payment.payments'))

@payment_bp.route('/edit_payment/<int:id>', methods=['POST'])
def edit_payment(id):
    p = session.get(Payment, id)
    data = request.form
    p.booking_id = int(data['booking_id'])
    p.amount = float(data['amount'])
    p.status = data['status']
    session.commit()
    return redirect(url_for('payment.payments'))