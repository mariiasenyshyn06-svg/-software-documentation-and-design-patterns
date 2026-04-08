from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from airbnb_lab2.app.config.db import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Owner(User):
    __tablename__ = "owners"
    owner_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)

class Housing(Base):
    __tablename__ = "housing"
    housing_id = Column(Integer, primary_key=True)
    address = Column(String)
    price = Column(Float)
    rooms = Column(Integer)

    photos = relationship("Photo", back_populates="housing")
    reviews = relationship("Review", back_populates="housing")

class Photo(Base):
    __tablename__ = "photos"
    photo_id = Column(Integer, primary_key=True)
    url = Column(String)
    description = Column(String)
    housing_id = Column(Integer, ForeignKey("housing.housing_id"))
    housing = relationship("Housing", back_populates="photos")

class Review(Base):
    __tablename__ = "reviews"
    review_id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    housing_id = Column(Integer, ForeignKey("housing.housing_id"))
    housing = relationship("Housing", back_populates="reviews")

class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    housing_id = Column(Integer, ForeignKey("housing.housing_id"))

class Payment(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True)
    amount = Column(Float)
    status = Column(String)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))