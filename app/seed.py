#!/usr/bin/env python3

from faker import Faker
from sqlalchemy.orm import sessionmaker
from model import engine, User,BMIRecord

fake= Faker()
Session = sessionmaker(bind=engine)
session = Session()

#to delete records

# session.query(User).delete()
# session.query(BMIRecord).delete()

# user =[
#     User (name = fake.name(),
#           age = fake.random_int(),
#           gender = fake.name()
#           )
#     for _ in range(12)
# ]
# session.add_all(user)

# session.commit()
# session.close()

# fake= Faker()
# session=sessionmaker(bind=engine)
# session= session()

# BMIRecord= [
#     BMIRecord (weight = fake.random_int(min=18, max=200),
#                height = fake.random_digit(),
#                bmi = fake.random_digit(),
#                classification = fake.name(),
#                user_id = fake.random_int()
#                )

#     for _ in range(10)
               
    
# ]
# session.add_all(BMIRecord)
session.commit()
session.close()

    



   



