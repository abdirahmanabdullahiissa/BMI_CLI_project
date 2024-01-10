import click
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime

Base = declarative_base()

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

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter your name', help='Your name')
@click.option('--age', prompt='Enter your age', type=int, help='Your age')
@click.option('--gender', prompt='Enter your gender', help='Your gender')
@click.option('--weight', prompt='Enter your weight in kg', type=float, help='Your weight in kilograms')
@click.option('--height', prompt='Enter your height in meters', type=float, help='Your height in meters')
def calculate_bmi(name, age, gender, weight, height):
    engine = create_engine('sqlite:///bmi_database.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(name=name, age=age, gender=gender)
    session.add(user)
    session.commit()

    bmi = weight / (height ** 2)
    classification = classify_bmi(bmi)

    bmi_record = BMIRecord(
        weight=weight,
        height=height,
        bmi=bmi,
        classification=classification,
        user=user
    )
    session.add(bmi_record)
    session.commit()

    click.echo(f"Your BMI: {bmi:.2f}")
    click.echo(f"Classification: {classification}")

    session.close()

@cli.command()
def view_history():
    engine = create_engine('sqlite:///bmi_database.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(User).all()

    click.echo("User Information:")
    for user in users:
        click.echo(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}, Gender: {user.gender}")

        for record in user.bmi_records:
            click.echo(
                f"  - BMI Record ID: {record.id} - BMI: {record.bmi:.2f}, Classification: {record.classification}"
            )

    session.close()

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
    cli()
