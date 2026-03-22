# Лабораторна 2: Airbnb (Python, SQLAlchemy)

Ця лабораторна демонструє створення серверної частини аплікації Airbnb з трирівневою архітектурою:

- Рівень доступу до даних (DAO/Repository)
- Рівень бізнес-логіки (Services)
- Презентаційний рівень (інтерфейси, без логіки)

Дані зберігаються в SQLite базі даних і можуть бути згенеровані з CSV файлів.

---

## Запуск проекту

1. Клонувати репозиторій:

git clone https://github.com/mariiasenyshyn06-svg/-software-documentation-and-design-patterns.git

2. Перейти у папку проекту:

cd -software-documentation-and-design-patterns/airbnb_lab2

3. Встановити залежності:

pip install sqlalchemy

4. Запустити генерацію даних та створення бази:

python3 main.py

---

## Структура проекту

airbnb_lab2/
├── app/
│   ├── config/          # Конфігурація бази
│   ├── dao/             # Репозиторії і інтерфейси
│   ├── entities/        # ORM моделі
│   └── services/        # Бізнес-логіка
├── utils/
│   └── csv_generator.py # Генерація CSV файлів
├── main.py              # Точка входу
├── README.md
└── .gitignore

---

## Функціонал

- Генерація >1000 записів у CSV
- Створення SQLite бази `airbnb.db`
- Наповнення таблиць: `users`, `owners`, `housing`, `photos`, `reviews`, `bookings`, `payments`