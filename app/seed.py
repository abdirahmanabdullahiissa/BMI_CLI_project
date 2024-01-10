#!/usr/bin/env python3

from faker import Faker
from sqlalchemy.orm import sessionmaker
from model import engine, User,BMIRecord

fake= Faker()
Session = sessionmaker(bind=engine)
session = Session()

user =[
    User (name = fake.name(),
          age = fake.random_int(),
          gender = fake.name()
          )
    for _ in range(5)
]

bmi_records = [
    bmi_records=(weight= fake.random_int(),
                 height= fake.random_int
                 bmi= )

]
session.add_all(user)

session.commit()
session.close()

    



   



