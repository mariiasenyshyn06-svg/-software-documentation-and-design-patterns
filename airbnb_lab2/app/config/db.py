from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///airbnb.db', echo=True)  # Можна змінити на MySQL
SessionLocal = sessionmaker(bind=engine)