from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    duration_nights = Column(Integer, nullable=False)

    # Relationships
    days = relationship("Day", back_populates="itinerary", cascade="all, delete-orphan")

class Day(Base):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer, nullable=False)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id', ondelete="CASCADE"), nullable=False)

    # Relationships
    itinerary = relationship("Itinerary", back_populates="days")
    hotel = relationship("HotelAccommodation", uselist=False, back_populates="day", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="day", cascade="all, delete-orphan")
    transfers = relationship("Transfer", back_populates="day", cascade="all, delete-orphan")

class HotelAccommodation(Base):
    __tablename__ = "hotel_accommodations"

    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    day_id = Column(Integer, ForeignKey('days.id', ondelete="CASCADE"), nullable=False)

    # Relationships
    day = relationship("Day", back_populates="hotel")

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String, nullable=True)
    day_id = Column(Integer, ForeignKey('days.id', ondelete="CASCADE"), nullable=False)

    # Relationships
    day = relationship("Day", back_populates="activities")

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    origin = Column(String, nullable=True)
    destination = Column(String, nullable=True)
    day_id = Column(Integer, ForeignKey('days.id', ondelete="CASCADE"), nullable=False)

    # Relationships
    day = relationship("Day", back_populates="transfers")
