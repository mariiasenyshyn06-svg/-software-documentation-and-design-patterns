import csv
from sqlalchemy.orm import Session
from airbnb_lab2.app.models.entities import User, Housing, Booking, Payment
from airbnb_lab2.app.dao.interfaces import IUserDAO, IHousingDAO, IBookingDAO, IPaymentDAO

# ===== User =====
class UserRepository(IUserDAO):
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def get_all_users(self):
        return self.session.query(User).all()

    def load_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user = User(name=row['name'], email=row['email'], password=row['password'])
                self.add_user(user)

# ===== Housing =====
class HousingRepository(IHousingDAO):
    def __init__(self, session: Session):
        self.session = session

    def add_housing(self, housing: Housing):
        self.session.add(housing)
        self.session.commit()

    def get_all_housing(self):
        return self.session.query(Housing).all()

    def load_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                housing = Housing(address=row['address'], price=float(row['price']), rooms=int(row['rooms']))
                self.add_housing(housing)

# ===== Booking =====
class BookingRepository(IBookingDAO):
    def __init__(self, session: Session):
        self.session = session

    def add_booking(self, booking: Booking):
        self.session.add(booking)
        self.session.commit()

    def get_all_bookings(self):
        return self.session.query(Booking).all()

    def load_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                booking = Booking(
                    user_id=int(row['user_id']),
                    housing_id=int(row['housing_id']),
                    status=row['status']
                )
                self.add_booking(booking)

# ===== Payment =====
class PaymentRepository(IPaymentDAO):
    def __init__(self, session: Session):
        self.session = session

    def add_payment(self, payment: Payment):
        self.session.add(payment)
        self.session.commit()

    def get_all_payments(self):
        return self.session.query(Payment).all()

    def load_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                payment = Payment(
                    booking_id=int(row['booking_id']),
                    amount=float(row['amount']),
                    status=row['status']
                )
                self.add_payment(payment)