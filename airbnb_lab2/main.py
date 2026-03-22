from airbnb_lab2.app.config.db import Base, engine, SessionLocal
from airbnb_lab2.app.dao.repository import UserRepository, HousingRepository, BookingRepository, PaymentRepository
from airbnb_lab2.app.services.service import AirbnbService
from airbnb_lab2.utils.csv_generator import generate_csv

# 1. Генеруємо CSV файли
generate_csv(n=1000)

# 2. Створюємо таблиці
Base.metadata.create_all(engine)

# 3. Створюємо сесію
session = SessionLocal()

# 4. Ініціалізуємо репозиторії
user_repo = UserRepository(session)
housing_repo = HousingRepository(session)
booking_repo = BookingRepository(session)
payment_repo = PaymentRepository(session)

# 5. Ініціалізуємо сервіс
service = AirbnbService(user_repo, housing_repo, booking_repo, payment_repo)

# 6. Завантажуємо дані
service.load_all_data(
    'data/users.csv',
    'data/housing.csv',
    'data/bookings.csv',
    'data/payments.csv'
)

print("Готово! База даних заповнена 1000+ записами.")