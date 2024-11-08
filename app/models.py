from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    occupation = Column(String)
    fcm_token = Column(String)
    events = relationship("Event", back_populates="user")
    reminders = relationship("Reminder", back_populates="user")

class Event(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(Date)
    location_id = Column(Integer, ForeignKey('locations.id'))
    user_id = Column(String, ForeignKey('users.user_id'))
    user = relationship("User", back_populates="events")
    items = relationship("Item", back_populates="event")

class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.event_id'))
    is_checked = Column(Boolean, default=False)
    notes = Column(String)
    event = relationship("Event", back_populates="items")

class Reminder(Base):
    __tablename__ = "reminders"
    reminder_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.user_id'))
    title = Column(String, index=True)
    schedule_date = Column(Date)
    is_active = Column(Boolean, default=True)
    message = Column(String)
    user = relationship("User", back_populates="reminders")

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)