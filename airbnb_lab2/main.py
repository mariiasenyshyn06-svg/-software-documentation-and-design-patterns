from airbnb_lab2.app.config.db import Base, engine, SessionLocal
from airbnb_lab2.app.dao.repository import UserRepository, HousingRepository, BookingRepository, PaymentRepository
from airbnb_lab2.app.services.service import AirbnbService
from airbnb_lab2.utils.csv_generator import generate_csv

generate_csv(n=1000)
print("CSV файли згенеровані у папці data/")

Base.metadata.create_all(engine)
print("Таблиці створені у базі airbnb.db")

session = SessionLocal()

user_repo = UserRepository(session)
housing_repo = HousingRepository(session)
booking_repo = BookingRepository(session)
payment_repo = PaymentRepository(session)

service = AirbnbService(user_repo, housing_repo, booking_repo, payment_repo)

service.load_all_data(
    'data/users.csv',
    'data/housing.csv',
    'data/bookings.csv',
    'data/payments.csv'
)

print("Готово! База даних airbnb.db заповнена 1000+ записами.")