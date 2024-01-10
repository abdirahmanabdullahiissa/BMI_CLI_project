from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///bmi_database.db')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    bmi_records = relationship('BMIRecord', back_populates='user')

class BMIRecord(Base):
    __tablename__ = 'bmi_records'

    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    height = Column(Float)
    bmi = Column(Float)
    classification = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='bmi_records')





