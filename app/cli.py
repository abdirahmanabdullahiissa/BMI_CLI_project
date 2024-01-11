import random
import click
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime
from model import engine,User, BMIRecord
from seed import session


@click.group()
def cli():
    pass

@cli.command()

def user():

    name = click.prompt('Enter your name')
    age =  click.prompt('Enter your age')
    gender = click.prompt('Enter your gender')
    # weight= click.prompt('Enter your weight in kg')
    # height= click.prompt('Enter your height in meters')

    new_record = User(name=name,age=age,gender=gender)
    session.add(new_record)
    session.commit()
    

    click.echo (f"name{name},age{age},gender{gender}")
# @cli.command()
# def bmi():
#      weight= click.prompt('Enter your weight in kg')
#      height= click.prompt('Enter your height in meters')
#      bmi = int(weight) / int(height)

     
#      new_bmi= BMIRecord(weight=weight,height=height,bmi=bmi)
#      session.add(new_bmi)
#      session.commit()
     
#      click.echo (f"weight{weight},height{height},bmi{bmi}")

@cli.command()
def classify():
    weight = click.prompt('Enter your weight in kg')
    height = click.prompt('Enter your height in meters')
    bmi = int(weight) / int(height)
    users = session.query(User).all()


    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi < 25:
        classification = "Normal weight"
    elif 25 <= bmi < 30:
        classification = "Overweight"
    else:
        classification = "Obese"

    if users:
        user_ids = []
        for i in range(len(users)):
            user_ids.append(users[i].id)
        
        new_classification = BMIRecord( weight=weight,height=height,bmi=bmi,classification=classification, user_id= random.choice(user_ids))
        session.add(new_classification)
        session.commit()

    click.echo(f"Weight: {weight}, Height: {height}, BMI: {bmi}, Classification: {classification}")


   



if __name__ == '__main__':
    cli.add_command(user)
    cli.add_command(classify)
    cli()
